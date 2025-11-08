import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import turtle
import colorsys

# ==========================================
# 1. COLORFUL SPIRAL FLOWER (Polar Coordinates)
# ==========================================

def spiral_flower(n_petals=8, n_spirals=5, colors=['#FF1493', '#FF69B4', '#FFB6C1', '#FFC0CB']):
    """
    Create a beautiful spiral flower using polar coordinates
    
    Parameters:
    - n_petals: Number of petals
    - n_spirals: Number of spiral layers
    - colors: List of colors for gradients
    """
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Create multiple spiral layers with different colors
    for i in range(n_spirals):
        # Create petal shape using sine waves
        r = 1 + 0.5 * np.sin(n_petals * theta) * np.exp(-i * 0.1)
        
        # Add some variation to each spiral
        r += 0.2 * np.sin(theta * (i + 1) * 2)
        
        # Select color from gradient
        color = colors[i % len(colors)]
        alpha = 1.0 - (i * 0.15)  # Fade outer spirals
        
        ax.plot(theta, r, color=color, linewidth=2, alpha=alpha)
        ax.fill(theta, r, color=color, alpha=alpha * 0.3)
    
    # Add center circle
    center_theta = np.linspace(0, 2 * np.pi, 100)
    center_r = np.ones(100) * 0.3
    ax.fill(center_theta, center_r, color='#FFD700', alpha=0.9)
    
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_title('Spiral Flower', fontsize=20, pad=20, fontweight='bold')
    plt.tight_layout()
    return fig

# ==========================================
# 2. GEOMETRIC FLOWER (Turtle Graphics)
# ==========================================

def geometric_flower_turtle(n_petals=12, petal_size=100, colors=None):
    """
    Create a geometric flower pattern using turtle graphics
    
    Parameters:
    - n_petals: Number of petals
    - petal_size: Size of each petal
    - colors: List of colors to cycle through
    """
    if colors is None:
        colors = ['#FF1493', '#FF69B4', '#FFB6C1', '#BA55D3', '#DA70D6', '#EE82EE']
    
    # Setup
    screen = turtle.Screen()
    screen.bgcolor('#F0F8FF')
    screen.title('Geometric Flower Pattern')
    
    flower = turtle.Turtle()
    flower.speed(0)  # Fastest
    flower.width(2)
    
    # Draw petals
    angle = 360 / n_petals
    
    for i in range(n_petals):
        flower.color(colors[i % len(colors)])
        flower.begin_fill()
        
        # Draw petal shape (circle)
        flower.circle(petal_size)
        
        flower.end_fill()
        flower.right(angle)
    
    # Draw center
    flower.penup()
    flower.goto(0, -30)
    flower.pendown()
    flower.color('#FFD700')
    flower.begin_fill()
    flower.circle(30)
    flower.end_fill()
    
    flower.hideturtle()
    screen.mainloop()

# ==========================================
# 3. SUNFLOWER (Fibonacci Spiral)
# ==========================================

def fibonacci_sunflower(n_seeds=500, scale=5, colors='viridis'):
    """
    Create a sunflower using Fibonacci spiral pattern
    
    Parameters:
    - n_seeds: Number of seeds in the pattern
    - scale: Scale factor for size
    - colors: Colormap for the seeds
    """
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#87CEEB')
    
    # Golden angle in radians
    golden_angle = np.pi * (3 - np.sqrt(5))
    
    # Generate Fibonacci spiral points
    theta = np.arange(0, n_seeds) * golden_angle
    r = scale * np.sqrt(np.arange(0, n_seeds))
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Create color gradient based on distance from center
    colors_array = plt.cm.YlOrBr(np.linspace(0.2, 0.9, n_seeds))
    
    # Draw seeds
    sizes = np.linspace(200, 50, n_seeds)  # Larger seeds in center
    ax.scatter(x, y, c=colors_array, s=sizes, alpha=0.9, edgecolors='#8B4513', linewidth=1)
    
    # Add petals around the edge
    n_petals = 20
    petal_angle = np.linspace(0, 2 * np.pi, n_petals, endpoint=False)
    petal_r = scale * np.sqrt(n_seeds) + 10
    
    for angle in petal_angle:
        # Create petal shape
        petal_theta = np.linspace(-0.3, 0.3, 50) + angle
        petal_length = np.linspace(0, 15, 50)
        petal_width = 15 * np.exp(-((np.linspace(-0.3, 0.3, 50)) ** 2) / 0.1)
        
        px = (petal_r + petal_length) * np.cos(petal_theta)
        py = (petal_r + petal_length) * np.sin(petal_theta)
        
        ax.fill(px, py, color='#FFD700', alpha=0.8, edgecolor='#FFA500', linewidth=2)
    
    ax.set_xlim(-petal_r - 20, petal_r + 20)
    ax.set_ylim(-petal_r - 20, petal_r + 20)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Fibonacci Sunflower', fontsize=20, pad=20, fontweight='bold')
    plt.tight_layout()
    return fig

# ==========================================
# 4. ROSE CURVE (Parametric Equations)
# ==========================================

def rose_curve(n_petals=7, k=5, colors='gradient'):
    """
    Create a rose curve using parametric equations
    
    Parameters:
    - n_petals: Number of petals (use odd numbers for better results)
    - k: Parameter for rose curve complexity
    - colors: 'gradient' or list of colors
    """
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#FFF5EE')
    
    theta = np.linspace(0, 2 * np.pi * k, 2000)
    
    # Rose curve: r = cos(n*theta)
    r = np.cos(n_petals * theta)
    
    # Convert to Cartesian
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Create color gradient along the curve
    if colors == 'gradient':
        # Rainbow gradient
        colors_array = [colorsys.hsv_to_rgb(i/len(theta), 0.8, 0.9) for i in range(len(theta))]
    else:
        colors_array = colors
    
    # Plot with gradient colors
    for i in range(len(x) - 1):
        ax.plot(x[i:i+2], y[i:i+2], color=colors_array[i], linewidth=2, alpha=0.8)
    
    # Fill the rose
    ax.fill(x, y, color='#FF69B4', alpha=0.2)
    
    # Add decorative center
    center_circle = Circle((0, 0), 0.1, color='#FF1493', zorder=10)
    ax.add_patch(center_circle)
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'Rose Curve (n={n_petals})', fontsize=20, pad=20, fontweight='bold')
    plt.tight_layout()
    return fig

# ==========================================
# 5. MULTIPLE FLOWERS WITH GRADIENTS
# ==========================================

def multiple_gradient_flowers(n_flowers=5):
    """
    Create multiple flowers with different petal counts and gradient colors
    """
    fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw=dict(projection='polar'))
    fig.patch.set_facecolor('#FFF8DC')
    axes = axes.flatten()
    
    petal_counts = [3, 5, 7, 9, 12, 16]
    
    for idx, (ax, n_petals) in enumerate(zip(axes, petal_counts)):
        theta = np.linspace(0, 2 * np.pi, 1000)
        
        # Create petal shape
        r = (1 + 0.5 * np.sin(n_petals * theta)) * (1 + 0.1 * np.sin(20 * theta))
        
        # Generate gradient colors
        hue_start = idx / len(petal_counts)
        colors_array = [colorsys.hsv_to_rgb((hue_start + i/1000) % 1, 0.8, 0.95) 
                       for i in range(1000)]
        
        # Plot with gradient
        for i in range(len(theta) - 1):
            ax.plot(theta[i:i+2], r[i:i+2], color=colors_array[i], linewidth=2)
        
        # Fill with semi-transparent color
        fill_color = colorsys.hsv_to_rgb(hue_start, 0.6, 0.9)
        ax.fill(theta, r, color=fill_color, alpha=0.3)
        
        # Add center
        center_theta = np.linspace(0, 2 * np.pi, 100)
        center_r = np.ones(100) * 0.2
        ax.fill(center_theta, center_r, color='#FFD700', alpha=0.9, edgecolor='#FF8C00', linewidth=2)
        
        ax.set_ylim(0, 1.8)
        ax.axis('off')
        ax.set_title(f'{n_petals} Petals', fontsize=14, pad=10, fontweight='bold')
    
    fig.suptitle('Garden of Gradient Flowers', fontsize=22, fontweight='bold', y=0.98)
    plt.tight_layout()
    return fig

# ==========================================
# BONUS: Customizable Flower Function
# ==========================================

def custom_flower(n_petals=8, petal_length=1.5, petal_width=0.5, 
                 rotation=0, color='#FF69B4', center_color='#FFD700'):
    """
    Create a fully customizable flower
    
    Parameters:
    - n_petals: Number of petals
    - petal_length: Length of each petal
    - petal_width: Width of each petal
    - rotation: Rotation angle in degrees
    - color: Petal color
    - center_color: Center color
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#F0F8FF')
    
    # Draw petals
    for i in range(n_petals):
        angle = (360 / n_petals * i + rotation) * np.pi / 180
        
        # Create petal shape (ellipse-like)
        t = np.linspace(0, 2 * np.pi, 100)
        petal_x = petal_width * np.cos(t) * 0.5
        petal_y = petal_length * np.sin(t) * 0.5
        
        # Rotate petal
        x = petal_x * np.cos(angle) - petal_y * np.sin(angle)
        y = petal_x * np.sin(angle) + petal_y * np.cos(angle)
        
        # Move petal outward
        offset = 0.5
        x += offset * np.cos(angle)
        y += offset * np.sin(angle)
        
        ax.fill(x, y, color=color, alpha=0.7, edgecolor='#FF1493', linewidth=2)
    
    # Draw center
    center = Circle((0, 0), 0.3, color=center_color, zorder=10, edgecolor='#FFA500', linewidth=3)
    ax.add_patch(center)
    
    # Add small dots in center
    n_dots = 20
    dot_angles = np.linspace(0, 2 * np.pi, n_dots, endpoint=False)
    for angle in dot_angles:
        dot_x = 0.15 * np.cos(angle)
        dot_y = 0.15 * np.sin(angle)
        dot = Circle((dot_x, dot_y), 0.03, color='#8B4513', zorder=11)
        ax.add_patch(dot)
    
    ax.set_title('Custom Flower', fontsize=20, pad=20, fontweight='bold')
    plt.tight_layout()
    return fig

# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # Generate all flower visualizations
    
    print("Generating flower visualizations...")
    
    # 1. Spiral Flower
    print("1. Creating spiral flower...")
    fig1 = spiral_flower(n_petals=12, n_spirals=7, 
                         colors=['#FF1493', '#FF69B4', '#FFB6C1', '#FFC0CB', '#DDA0DD'])
    plt.savefig('spiral_flower.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    
    # 2. Geometric Flower (Turtle) - Uncomment to run
    # Note: Turtle creates a separate window
    # print("2. Creating geometric flower (turtle graphics)...")
    # geometric_flower_turtle(n_petals=16, petal_size=80)
    
    # 3. Fibonacci Sunflower
    print("3. Creating Fibonacci sunflower...")
    fig3 = fibonacci_sunflower(n_seeds=600, scale=5)
    plt.savefig('fibonacci_sunflower.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. Rose Curve
    print("4. Creating rose curve...")
    fig4 = rose_curve(n_petals=5, k=3)
    plt.savefig('rose_curve.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 5. Multiple Gradient Flowers
    print("5. Creating multiple gradient flowers...")
    fig5 = multiple_gradient_flowers()
    plt.savefig('gradient_flowers.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Bonus: Custom Flower
    print("Bonus: Creating custom flower...")
    fig6 = custom_flower(n_petals=10, petal_length=1.8, petal_width=0.6,
                        rotation=15, color='#DA70D6', center_color='#FFD700')
    plt.savefig('custom_flower.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\nAll visualizations complete!")
    print("Images saved as PNG files.")
    
    # Example customizations:
    print("\n" + "="*50)
    print("CUSTOMIZATION EXAMPLES:")
    print("="*50)
    print("\n# Create a 20-petal spiral flower with custom colors:")
    print("spiral_flower(n_petals=20, n_spirals=10, colors=['#FF0000', '#00FF00', '#0000FF'])")
    print("\n# Create a geometric flower with 24 petals:")
    print("geometric_flower_turtle(n_petals=24, petal_size=60)")
    print("\n# Create a dense sunflower:")
    print("fibonacci_sunflower(n_seeds=1000, scale=6)")
    print("\n# Create a complex rose curve:")
    print("rose_curve(n_petals=11, k=7)")
    print("\n# Create your own custom flower:")
    print("custom_flower(n_petals=6, petal_length=2.0, petal_width=0.8, color='#FF1493')")
