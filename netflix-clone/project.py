import google.generativeai as genai
import os
from PIL import Image
import requests
from io import BytesIO

# Configure the Gemini API
API_KEY = 'AIzaSyD6D09v7G_iQObEZYn7ZC4uRa-qlC3h96E'  # Please replace this with a new, secure key
genai.configure(api_key=API_KEY)

def generate_story(character, moral):
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Write a short story featuring a character named {character} with the moral: '{moral}'. The story should be suitable for all ages."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating story: {e}")
        return None

def generate_image(scene_description):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        prompt = f"Generate an image of the following scene: {scene_description}"
        response = model.generate_content(prompt)
        
        # Note: This is a placeholder. The actual implementation will depend on
        # how Gemini API returns image data. You may need to adjust this.
        image_data = response.image
        img = Image.open(BytesIO(image_data))
        return img
    except Exception as e:
        print(f"Error generating image: {e}")
        print("Using a placeholder image instead.")
        placeholder_url = "https://via.placeholder.com/300x200.png?text=Story+Scene"
        response = requests.get(placeholder_url)
        return Image.open(BytesIO(response.content))

def save_story_and_image(story, image):
    try:
        with open("generated_story.txt", "w", encoding='utf-8') as f:
            f.write(story)
        image.save("story_illustration.png")
        print("\nStory saved as 'generated_story.txt' and illustration saved as 'story_illustration.png'")
    except Exception as e:
        print(f"Error saving story or image: {e}")

def main():
    character = input("Enter the main character's name: ")
    moral = input("Enter the moral of the story: ")
    
    story = generate_story(character, moral)
    if story:
        print("\nGenerated Story:")
        print(story)
        
        scene_description = input("\nDescribe a key scene from the story for illustration: ")
        image = generate_image(scene_description)
        
        if image:
            image.show()
            save_story_and_image(story, image)
    else:
        print("Failed to generate the story. Please try again.")

if __name__ == "__main__":
    main()