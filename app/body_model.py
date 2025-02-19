import pyvista as pv
import base64
import os

def generate_3d_image_base64(model_path):
    """Generates a base64 encoded PNG image of the 3D model.

    Args:
        model_path (str): Path to the 3D model file.

    Returns:
        str: Base64 encoded PNG data, or an error message.
    """
    if not os.path.exists(model_path):
        return "Error: Model file not found."

    try:
        mesh = pv.read(model_path)
        plotter = pv.Plotter(offscreen=True)
        plotter.add_mesh(mesh, smooth_shading=True, lighting=True,
                         ambient_color=(0.3, 0.3, 0.3),
                         diffuse_color=(0.7, 0.7, 0.7),
                         specular_color=(0.3, 0.3, 0.3),
                         specular_power=20)
        bounds = mesh.bounds
        center = mesh.center
        camera_position = (center[0] * 1.5, center[1] * 1.5, bounds[5] * 2)
        plotter.camera_position = camera_position
        plotter.camera_focal_point = center

        png_data = plotter.screenshot(return_img=True)
        png_base64 = base64.b64encode(png_data).decode("utf-8")
        return png_base64

    except Exception as e:
        return f"An error occurred: {e}"



def display_3d_body_embedded(model_path): # this function is no more used
        """Displays a 3D body model and embeds it in a webpage.

        Args:
            model_path (str): The path to the 3D model file.
        """
        if not os.path.exists(model_path):
            return "Error: Model file not found."

        try:
            mesh = pv.read(model_path)
            plotter = pv.Plotter(offscreen=True)  # Important for web embedding
            plotter.add_mesh(mesh, smooth_shading=True, lighting=True,
                             ambient_color=(0.3, 0.3, 0.3),
                             diffuse_color=(0.7, 0.7, 0.7),
                             specular_color=(0.3, 0.3, 0.3),
                             specular_power=20)

            bounds = mesh.bounds
            center = mesh.center
            camera_position = (center[0] * 1.5, center[1] * 1.5, bounds[5] * 2)
            plotter.camera_position = camera_position
            plotter.camera_focal_point = center

            # Render to PNG in memory (no file needed)
            png_data = plotter.screenshot(return_img=True)

            # Encode to base64 for embedding in HTML
            png_base64 = base64.b64encode(png_data).decode("utf-8")

            # Create the HTML string with embedded image
            html_string = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>3D Body Model</title>
            </head>
            <body>
            <img src="data:image/png;base64,{png_base64}" alt="3D Body Model">
            </body>
            </html>
            """

            return html_string

        except Exception as e:
            return f"An error occurred: {e}"