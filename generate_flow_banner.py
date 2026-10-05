import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# LinkedIn Cover proportions: 1584 x 396 (4:1 aspect ratio)
WIDTH_PX, HEIGHT_PX = 1584, 396
DPI = 100
WIDTH_IN, HEIGHT_IN = WIDTH_PX / DPI, HEIGHT_PX / DPI

def setup_figure():
    """Sets up the canvas with exact LinkedIn dimensions and a white background."""
    fig = plt.figure(figsize=(WIDTH_IN, HEIGHT_IN), dpi=DPI)
    fig.patch.set_facecolor('#ffffff') # White background
    
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    return fig, ax

def generate_flow_field():
    fig, ax = setup_figure()
    
    # 1. Create a dense grid of X and Y coordinates
    Y, X = np.mgrid[-3:3:100j, -10:10:300j]
    
    # 2. Define the Vector Field mathematically
    # Try changing the multipliers (e.g., 1.5 to 2.0) or swapping sin/cos to see how the flow changes!
    U = X / (X**2 + Y**2 + 0.1) - (X - 2) / ((X - 2)**2 + Y**2 + 0.1)
    V = Y / (X**2 + Y**2 + 0.1) - Y / ((X - 2)**2 + Y**2 + 0.1)
    
    # Calculate the overall speed at each point
    speed = np.sqrt(U**2 + V**2)
    
    # 3. Plot the streamplot
    # Try changing `cmap` to 'inferno', 'plasma', 'viridis', or 'magma'
    lw = 1.5 * speed / speed.max() + 0.2
    ax.streamplot(X, Y, U, V, color=speed, linewidth=lw, cmap='winter', density=6.9, arrowstyle='-', arrowsize=0)
    
    # Save the output image
    output_filename = 'linkedin_flow_banner.png'
    plt.savefig(output_filename, facecolor=fig.get_facecolor(), dpi=DPI)
    print(f"Successfully generated {output_filename}")
    plt.close()

if __name__ == '__main__':
    generate_flow_field()
