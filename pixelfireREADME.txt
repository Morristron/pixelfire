Pixel Fire Effect

Author: Morris Bartlett

Overview

pixelfire.py is a Python script that generates a pixel-based fire effect using the Pygame library. This dynamic and visually appealing effect simulates fire by updating pixel colors over time based on a predefined palette. The script is lightweight, easy to integrate, and ideal for use in games or creative projects.

Features

Realistic Fire Simulation: Implements a decay-based algorithm for flickering flames.

Customizable Resolution: Adjust fire resolution and screen dimensions for performance or aesthetic needs.

Lightweight Rendering: Uses a scaled-up surface to optimize performance.

Extensible Design: Can be easily enhanced with interactive features or different palettes.

Installation

Ensure you have Python 3 installed.

Install Pygame by running:

pip install pygame

How to Run

Save the pixelfire.py file locally.

Run the script using:

python pixelfire.py

Enjoy the mesmerizing fire effect!

Usage

The script is designed to run out-of-the-box. By default, it displays a fire effect on an 800x600 screen. You can tweak the following parameters directly in the script:

screen_width and screen_height: Dimensions of the window.

fire_width and fire_height: Resolution of the fire effect.

palette: Color scheme for the fire effect.

How It Works

Fire Array: A 2D array (fire_array) stores the intensity of each pixel in the fire.

Palette: A predefined color palette maps intensity values to colors.

Fire Propagation:

Intensity values decay as they move upward.

New fire is randomly generated at the bottom row.

Rendering:

The fire array is rendered onto a small surface.

The surface is scaled up to fit the screen for pixelated visual effects.

Potential Enhancements

Interactive Features: Allow users to "feed" the fire by clicking on the screen.

Optimized Rendering: Use pygame.surfarray for faster rendering.

Custom Palettes: Support for dynamic color palettes.

Example Output

The effect creates a flickering fire graphic similar to retro games. Below is a scaled-up view of what the effect might look like:

[Pixelated flame graphic]

License

This project is licensed under the MIT License. Feel free to use and modify it for personal or commercial purposes.

Contributions

Contributions are welcome! If you'd like to add features or improve performance, feel free to fork the repository and submit a pull request.

Contact

For questions or feedback, please contact me at bartlett.morris@gmail.com.

