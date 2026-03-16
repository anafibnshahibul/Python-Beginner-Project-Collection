import qrcode
import os

def generate_custom_qr():
    """
    Generates a customized QR code based on user input for data, 
    colors, and filename.
    """
    print("=== Welcome to QR Code Generator ===")

    # Get data or URL from user
    input_data = input("\nEnter the URL or Text for the QR code: ").strip()
    if not input_data:
        print("Error: Input cannot be empty!")
        return

    # Get fill color (e.g., red, blue, black)
    fill_c = input("Enter fill color (default is 'black'): ").strip().lower() or "black"

    # Get background color
    back_c = input("Enter background color (default is 'white'): ").strip().lower() or "white"

    # Get filename for the output image
    file_name = input("Enter the filename to save (default is 'my_qrcode.png'): ").strip()
    
    # Set default filename if empty
    if not file_name:
        file_name = "my_qrcode.png"
    
    # Ensure the file has a .png extension
    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    # QR Code configuration settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    try:
        # Add data to the QR object
        qr.add_data(input_data)
        qr.make(fit=True)

        # Create the image with custom colors
        img = qr.make_image(fill_color=fill_c, back_color=back_c)
        
        # Save the generated image
        img.save(file_name)

        print(f"\nSuccessfully generated! Saved as: {file_name}")
        print(f"Details: Fill={fill_c}, Background={back_c}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_custom_qr()