import boto3

def detect_labels(photo, ingredients):
    session = boto3.Session(region_name='us-east-1')
    client = session.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()},
                                        MaxLabels=100,
                                        MinConfidence=30,
                                        Features=["GENERAL_LABELS"],
                                        Settings={"GeneralLabels": {"LabelCategoryInclusionFilters": ["Food and Beverage"]}}
                                        )

    labels = []

    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))

        labels.append(str(label['Name']).lower())

    print("Labels detected: " + str(len(response['Labels'])))

    print("------------------------------------------------------")
    if all(label in labels for label in ingredients):
        print("You have all the necessary ingredients for the recipe!")
    else:
        print("Oh no! You don't have all the ingredients!")


def main():
    ingredients = [x.lower() for x in input("Input the ingredients (comma separated): ").replace(" ", "").split(',')]

    photo = 'Fridge.jpg'

    detect_labels(photo, ingredients)


if __name__ == "__main__":
    main()
