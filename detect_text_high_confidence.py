import boto3 
import json

def get_text(image, bucket):

    highest_confidence_text = 0
    new_text = {}

    client = boto3.client('rekognition','us-east-1')

    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':image}})

    textDetections = response['TextDetections']

    for t in response['TextDetections']:
        print(t['DetectedText'] + ':' + str(t['Confidence']))
    
    print('Detected text\n----------')

    for text in textDetections:
        if highest_confidence_text < text['Confidence']:
            highest_confidence_text = text['Confidence']
            new_text = text
    print("")
    print('     Text with highest confidence -> ')
    print('     Detected text: ' + new_text['DetectedText'])
    print('     Confidence: ' + "{:.2f}".format(new_text['Confidence']) + "%")
    print('     Type: ' + new_text['Type'])
    print("")
    return len(textDetections)

def main():

    bucket = 'rekognition-canut'
    image = 'cartel4.jpg'
    text_count = get_text(image,bucket)
    print("Text detected: " + str(text_count))

if __name__ == "__main__":
    main()