from PIL import Image
import pytesseract


def extract_text(image_path):

    try:

        image = Image.open(
            image_path
        )

        text = (
            pytesseract
            .image_to_string(
                image
            )
        )

        return text

    except Exception as error:

        print(
            f"Error: {error}"
        )

        return ""


if __name__ == "__main__":

    image_path = input(
        "Enter UI Screenshot Path: "
    )

    text = extract_text(
        image_path
    )

    print(
        "\nDetected Text:\n"
    )

    print(text)
