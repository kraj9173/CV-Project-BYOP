import argparse,os
import torch,torch.nn as nn 
from torchvision import models, transforms
from PIL import Image

## this whole code is to implement the binary classification cat and dog class this is done my using the weights of trained mode on colab .

def prediction(image_path, model, device):

    transform = transforms.Compose([


transforms.Resize((224,224)),
transforms.ToTensor(),

transforms.Normalize(
            [0.485,0.456,0.406],
            [0.229,0.224,0.225]
        )
    ])

    image = Image.open(image_path).convert('RGB')

    image = transform(image)

  
    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        output = model(image)

    _, prediction = torch.max(output,1)

    labels = ['cat','dog']

    return labels[prediction.item()]
def loading(model_path):


    model = models.resnet18(weights = None)
    features = model.fc.in_features

    model.fc = nn.Linear(features, 2)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    
    model.load_state_dict(torch.load(model_path, map_location=device))

    model.to(device)
    model.eval()

    return model, device

def main():

   
    parser = argparse.ArgumentParser(                        # command line arguments##
    )

    parser.add_argument(
        "--input",
        required=True)

    parser.add_argument(
        "--model",
        default="trained_model/best_resnet18_cats_dogs.pth")

    parser.add_argument(
        "--output",
        default="output/")

    args = parser.parse_args()


   

    model, device = loading(args.model)    ## load model##


    result = prediction(args.input, model, device)
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    output= os.path.join(
          args.output,
        "predictions.txt"
    )

    with open(output,"a") as file:

      file.write(
            f"file: {os.path.basename(args.input)} | result: {result}\n"
        )

    print(f"prediction :- {result}")



if __name__ == "__main__":

    main()