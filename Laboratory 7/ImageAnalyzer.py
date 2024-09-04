import scrapy
from google.cloud import vision_v1
from collections import Counter
from scrapy.crawler import CrawlerProcess
import os
import sys
import matplotlib.pyplot as plt

images_folder = "images"
image_data = []

class ImageScraper(scrapy.Spider):
    name = "image_scraper"

    def __init__(self, url, *args, **kwargs):
        super(ImageScraper, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.images = []
        self.i = 0

    def parse(self, response):
        # Get the source of all the images in the page
        image_urls = response.css("img::attr(src)").getall()[:100]  # Limit to 100 images

        for image_url in image_urls:
            # Callback for all the urls fetched
            yield scrapy.Request(image_url, callback=self.download_image)

    def download_image(self, response):
        # Create images folder
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)

        # Create image file (the name is given by the index i to avoid errors caused by the images urls)
        image_name = os.path.basename(str(self.i))
        image_ext = ".jpg"
        image_path = os.path.join(images_folder, f"{image_name}{image_ext}")
        self.i = self.i + 1

        # Save image
        with open(image_path, "wb") as f:
            f.write(response.body)
        self.images.append(image_path)

        # Analyze image
        self.analyze_image(image_path)

    def analyze_image(self, image_name):
        # Create an ImageAnnotator client for Google Vision
        vision_client = vision_v1.ImageAnnotatorClient()

        # Read image from file
        with open(image_name, "rb") as image_file:
            content = image_file.read()

        image = vision_v1.Image(content=content)

        # Create request to get the labels detected in the image
        request = vision_v1.AnnotateImageRequest(image=image, features=[vision_v1.Feature(type_=vision_v1.types.Feature.Type.LABEL_DETECTION, max_results=10)])

        # Call the API to annotate the image
        response = vision_client.batch_annotate_images(requests=[request])
        labels = response.responses[0].label_annotations

        image_data_tmp = []
        # Save information about the labels
        for label in labels:
            description = label.description
            score = label.score
            image_data_tmp.append((description, score))
        image_data.append((image_name, image_data_tmp))

        # Delete the image in the folder
        os.remove(image_name)

def create_histogram(image_data):
    if not image_data:
        raise ValueError("No image data provided for histogram creation.")

    all_tags = []
    for image_name, tags in image_data:
        for tag, _ in tags:
            all_tags.append(tag)

    # Count the distinct tags from the ones fetched
    tag_counts = Counter(all_tags)

    # Find the 10 top tags
    top_tags = tag_counts.most_common(10)

    # Create the plots
    plt.figure(figsize=(10, 6))
    plt.bar([label for label, _ in top_tags], height=[count for _, count in top_tags], width=0.7, align='center')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Image Tags")
    plt.ylabel("Frequency")
    plt.title("Histogram of Most Frequent Image Tags")
    plt.tight_layout()
    plt.savefig("images/histogram.png")
    plt.close()

    print("Histogram saved as histogram.png")

def main():
    # Get the first argument from the command line
    try:
        url = sys.argv[1]
    except IndexError:
        print("Error: Please provide a URL as the first argument.")
        return

    # Start the crawler
    process = CrawlerProcess()
    process.crawl(ImageScraper, url=url)
    process.start()

    # Create the histogram with the data fetched
    create_histogram(image_data)

if __name__ == "__main__":
    main()