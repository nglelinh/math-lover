#!/usr/bin/env python3
"""
Generate visualizations for Fractions lesson (Chapter 04 - Halves and Quarters)
Demonstrates halves (1/2) and quarters (1/4) with various shapes and real-world examples
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Wedge, Polygon, FancyBboxPatch
import os

# Create output directory if it doesn't exist
output_dir = "../../img/chapter_img/chapter04"
os.makedirs(output_dir, exist_ok=True)

# Set style for child-friendly visuals
plt.style.use('seaborn-v0_8-bright')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F38181', '#95E1D3']

def create_halves_shapes():
    """
    Visualization 1: Different shapes divided into halves
    """
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    fig.suptitle('Halves (1/2): Splitting into 2 Equal Parts', 
                fontsize=18, fontweight='bold', y=0.98)
    
    shapes = [
        ('Circle', 'circle'),
        ('Square', 'square'),
        ('Rectangle', 'rectangle'),
        ('Triangle', 'triangle'),
        ('Pizza', 'pizza'),
        ('Sandwich', 'sandwich')
    ]
    
    for idx, (ax, (name, shape_type)) in enumerate(zip(axes.flat, shapes)):
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')
        ax.set_title(name, fontsize=14, fontweight='bold', pad=10)
        
        if shape_type == 'circle':
            # Left half
            wedge1 = Wedge((0, 0), 1, 90, 270, facecolor=colors[0], 
                          edgecolor='black', linewidth=3)
            ax.add_patch(wedge1)
            # Right half
            wedge2 = Wedge((0, 0), 1, 270, 90, facecolor=colors[1], 
                          edgecolor='black', linewidth=3)
            ax.add_patch(wedge2)
            # Dividing line
            ax.plot([0, 0], [-1, 1], 'k-', linewidth=3)
            
        elif shape_type == 'square':
            # Left half
            rect1 = Rectangle((-1, -1), 1, 2, facecolor=colors[2], 
                            edgecolor='black', linewidth=3)
            ax.add_patch(rect1)
            # Right half
            rect2 = Rectangle((0, -1), 1, 2, facecolor=colors[3], 
                            edgecolor='black', linewidth=3)
            ax.add_patch(rect2)
            # Dividing line
            ax.plot([0, 0], [-1, 1], 'k-', linewidth=3)
            
        elif shape_type == 'rectangle':
            # Top half
            rect1 = Rectangle((-1.2, 0), 2.4, 0.8, facecolor=colors[4], 
                            edgecolor='black', linewidth=3)
            ax.add_patch(rect1)
            # Bottom half
            rect2 = Rectangle((-1.2, -0.8), 2.4, 0.8, facecolor=colors[5], 
                            edgecolor='black', linewidth=3)
            ax.add_patch(rect2)
            # Dividing line
            ax.plot([-1.2, 1.2], [0, 0], 'k-', linewidth=3)
            
        elif shape_type == 'triangle':
            # Left half
            tri1 = Polygon([(-1, -0.8), (0, 1), (0, -0.8)], 
                          facecolor=colors[6], edgecolor='black', linewidth=3)
            ax.add_patch(tri1)
            # Right half
            tri2 = Polygon([(0, -0.8), (0, 1), (1, -0.8)], 
                          facecolor=colors[0], edgecolor='black', linewidth=3)
            ax.add_patch(tri2)
            # Dividing line
            ax.plot([0, 0], [-0.8, 1], 'k-', linewidth=3)
            
        elif shape_type == 'pizza':
            # Pizza circle
            circle = Circle((0, 0), 1, facecolor='#FFD700', 
                          edgecolor='#8B4513', linewidth=3)
            ax.add_patch(circle)
            # Toppings on left
            for _ in range(8):
                x = np.random.uniform(-0.8, -0.1)
                y = np.random.uniform(-0.6, 0.6)
                if x**2 + y**2 < 0.9:
                    pepperoni = Circle((x, y), 0.1, facecolor='red', 
                                     edgecolor='darkred', linewidth=1)
                    ax.add_patch(pepperoni)
            # Dividing line
            ax.plot([0, 0], [-1, 1], 'k-', linewidth=4, linestyle='--')
            
        elif shape_type == 'sandwich':
            # Bread top
            rect_top = Rectangle((-1, 0.3), 2, 0.3, facecolor='#DEB887', 
                                edgecolor='#8B4513', linewidth=2)
            ax.add_patch(rect_top)
            # Filling
            rect_fill = Rectangle((-1, -0.1), 2, 0.4, facecolor='#90EE90', 
                                 edgecolor='darkgreen', linewidth=1)
            ax.add_patch(rect_fill)
            # Bread bottom
            rect_bot = Rectangle((-1, -0.6), 2, 0.3, facecolor='#DEB887', 
                               edgecolor='#8B4513', linewidth=2)
            ax.add_patch(rect_bot)
            # Cut line (diagonal)
            ax.plot([-1, 1], [0.6, -0.6], 'k-', linewidth=3, linestyle='--')
        
        # Add fraction label
        ax.text(-0.5, -1.3, '1/2', ha='center', fontsize=16, fontweight='bold', color='blue')
        ax.text(0.5, -1.3, '1/2', ha='center', fontsize=16, fontweight='bold', color='blue')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/01_halves_shapes.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/01_halves_shapes.png")
    plt.close()


def create_quarters_shapes():
    """
    Visualization 2: Different shapes divided into quarters
    """
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    fig.suptitle('Quarters (1/4): Splitting into 4 Equal Parts', 
                fontsize=18, fontweight='bold', y=0.98)
    
    shapes = [
        ('Circle Pizza', 'circle'),
        ('Square Cake', 'square'),
        ('Rectangle', 'rectangle'),
        ('Paper Folded', 'paper'),
        ('Chocolate Bar', 'chocolate'),
        ('Orange', 'orange')
    ]
    
    for idx, (ax, (name, shape_type)) in enumerate(zip(axes.flat, shapes)):
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')
        ax.set_title(name, fontsize=14, fontweight='bold', pad=10)
        
        if shape_type == 'circle':
            # Four wedges
            wedge_colors = [colors[0], colors[1], colors[2], colors[3]]
            for i, (start_angle, color) in enumerate(zip([0, 90, 180, 270], wedge_colors)):
                wedge = Wedge((0, 0), 1, start_angle, start_angle + 90, 
                             facecolor=color, edgecolor='black', linewidth=3)
                ax.add_patch(wedge)
            # Dividing lines
            ax.plot([-1, 1], [0, 0], 'k-', linewidth=3)
            ax.plot([0, 0], [-1, 1], 'k-', linewidth=3)
            
        elif shape_type == 'square':
            # Four squares
            positions = [(-1, 0), (0, 0), (-1, -1), (0, -1)]
            for i, (x, y) in enumerate(positions):
                rect = Rectangle((x, y), 1, 1, facecolor=colors[i % len(colors)], 
                               edgecolor='black', linewidth=3)
                ax.add_patch(rect)
            
        elif shape_type == 'rectangle':
            # Four rectangles
            positions = [(-1.2, 0.4), (0, 0.4), (-1.2, -0.4), (0, -0.4)]
            for i, (x, y) in enumerate(positions):
                rect = Rectangle((x, y), 1.2, 0.4, facecolor=colors[(i+2) % len(colors)], 
                               edgecolor='black', linewidth=3)
                ax.add_patch(rect)
            
        elif shape_type == 'paper':
            # Paper with fold lines
            paper = Rectangle((-1, -1.2), 2, 2.4, facecolor='white', 
                            edgecolor='black', linewidth=3)
            ax.add_patch(paper)
            # Fold lines (dashed)
            ax.plot([-1, 1], [0, 0], 'k--', linewidth=2)
            ax.plot([0, 0], [-1.2, 1.2], 'k--', linewidth=2)
            # Color quarters lightly
            rect1 = Rectangle((-1, 0), 1, 1.2, facecolor=colors[4], alpha=0.3)
            ax.add_patch(rect1)
            rect2 = Rectangle((0, 0), 1, 1.2, facecolor=colors[5], alpha=0.3)
            ax.add_patch(rect2)
            rect3 = Rectangle((-1, -1.2), 1, 1.2, facecolor=colors[6], alpha=0.3)
            ax.add_patch(rect3)
            rect4 = Rectangle((0, -1.2), 1, 1.2, facecolor=colors[0], alpha=0.3)
            ax.add_patch(rect4)
            
        elif shape_type == 'chocolate':
            # Chocolate bar
            bar = Rectangle((-1.2, -0.8), 2.4, 1.6, facecolor='#6F4E37', 
                          edgecolor='black', linewidth=3)
            ax.add_patch(bar)
            # Dividing lines
            ax.plot([0, 0], [-0.8, 0.8], 'black', linewidth=2)
            ax.plot([-1.2, 1.2], [0, 0], 'black', linewidth=2)
            # Individual squares
            for i in range(2):
                for j in range(2):
                    x = -1.2 + i * 1.2
                    y = -0.8 + j * 0.8
                    inner_rect = Rectangle((x + 0.1, y + 0.1), 1.0, 0.6, 
                                          facecolor='#8B4513', edgecolor='none')
                    ax.add_patch(inner_rect)
            
        elif shape_type == 'orange':
            # Orange circle
            circle = Circle((0, 0), 1, facecolor='orange', 
                          edgecolor='darkorange', linewidth=3)
            ax.add_patch(circle)
            # Segments
            for angle in [0, 90, 180, 270]:
                rad = np.radians(angle)
                ax.plot([0, np.cos(rad)], [0, np.sin(rad)], 
                       'white', linewidth=3, linestyle='-')
        
        # Add fraction labels
        positions_text = [(-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)]
        for x, y in positions_text:
            ax.text(x, y, '1/4', ha='center', va='center', 
                   fontsize=14, fontweight='bold', color='darkblue')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/02_quarters_shapes.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/02_quarters_shapes.png")
    plt.close()


def create_half_vs_quarter_comparison():
    """
    Visualization 3: Compare size of 1/2 vs 1/4
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Which is Bigger: 1/2 or 1/4?', 
                fontsize=18, fontweight='bold', y=1.02)
    
    # Whole pizza
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.axis('off')
    ax1.set_title('Whole Pizza (1)', fontsize=14, fontweight='bold')
    
    circle = Circle((0, 0), 1, facecolor='#FFD700', 
                   edgecolor='#8B4513', linewidth=3)
    ax1.add_patch(circle)
    ax1.text(0, -1.3, '1 whole', ha='center', fontsize=14, fontweight='bold')
    
    # Half pizza
    ax2.set_aspect('equal')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.axis('off')
    ax2.set_title('Half Pizza (1/2)', fontsize=14, fontweight='bold')
    
    circle_full = Circle((0, 0), 1, facecolor='lightgray', alpha=0.3,
                        edgecolor='gray', linewidth=2, linestyle='--')
    ax2.add_patch(circle_full)
    wedge = Wedge((0, 0), 1, 90, 270, facecolor=colors[0], 
                 edgecolor='#8B4513', linewidth=3)
    ax2.add_patch(wedge)
    ax2.plot([0, 0], [-1, 1], 'k-', linewidth=3)
    ax2.text(0, -1.3, '1/2 (50%)', ha='center', fontsize=14, fontweight='bold', color=colors[0])
    
    # Quarter pizza
    ax3.set_aspect('equal')
    ax3.set_xlim(-1.5, 1.5)
    ax3.set_ylim(-1.5, 1.5)
    ax3.axis('off')
    ax3.set_title('Quarter Pizza (1/4)', fontsize=14, fontweight='bold')
    
    circle_full2 = Circle((0, 0), 1, facecolor='lightgray', alpha=0.3,
                         edgecolor='gray', linewidth=2, linestyle='--')
    ax3.add_patch(circle_full2)
    wedge2 = Wedge((0, 0), 1, 0, 90, facecolor=colors[2], 
                  edgecolor='#8B4513', linewidth=3)
    ax3.add_patch(wedge2)
    ax3.plot([-1, 1], [0, 0], 'k-', linewidth=3)
    ax3.plot([0, 0], [-1, 1], 'k-', linewidth=3)
    ax3.text(0, -1.3, '1/4 (25%)', ha='center', fontsize=14, fontweight='bold', color=colors[2])
    
    # Add conclusion
    fig.text(0.5, 0.05, '1/2 is BIGGER than 1/4 (more pizza for you!)', 
            ha='center', fontsize=16, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/03_half_vs_quarter.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/03_half_vs_quarter.png")
    plt.close()


def create_fractions_adding_up():
    """
    Visualization 4: Show how fractions add up to make a whole
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Fractions Add Up to Make a Whole!', 
                fontsize=18, fontweight='bold', y=0.98)
    
    # 1/2 + 1/2 = 1
    ax1 = axes[0, 0]
    ax1.set_aspect('equal')
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.axis('off')
    ax1.set_title('1/2 + 1/2 = 1 whole', fontsize=14, fontweight='bold')
    
    # First half
    wedge1 = Wedge((-1.5, 0), 0.8, 90, 270, facecolor=colors[0], 
                  edgecolor='black', linewidth=2)
    ax1.add_patch(wedge1)
    ax1.text(-1.5, -1.1, '1/2', ha='center', fontsize=12, fontweight='bold')
    
    # Plus sign
    ax1.text(-0.5, 0, '+', ha='center', va='center', fontsize=20, fontweight='bold')
    
    # Second half
    wedge2 = Wedge((0.5, 0), 0.8, 270, 90, facecolor=colors[1], 
                  edgecolor='black', linewidth=2)
    ax1.add_patch(wedge2)
    ax1.text(0.5, -1.1, '1/2', ha='center', fontsize=12, fontweight='bold')
    
    # Equals sign
    ax1.text(1.3, 0, '=', ha='center', va='center', fontsize=20, fontweight='bold')
    
    # Whole circle
    circle = Circle((2, 0), 0.8, facecolor='#FFD700', 
                   edgecolor='black', linewidth=2)
    ax1.add_patch(circle)
    ax1.text(2, -1.1, '1', ha='center', fontsize=12, fontweight='bold')
    
    # 1/4 + 1/4 + 1/4 + 1/4 = 1
    ax2 = axes[0, 1]
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.5, 6)
    ax2.set_ylim(-1.5, 1.5)
    ax2.axis('off')
    ax2.set_title('1/4 + 1/4 + 1/4 + 1/4 = 1 whole', fontsize=14, fontweight='bold')
    
    quarter_colors = [colors[2], colors[3], colors[4], colors[5]]
    for i in range(4):
        wedge = Wedge((i * 1.2, 0), 0.4, i * 90, (i + 1) * 90, 
                     facecolor=quarter_colors[i], edgecolor='black', linewidth=2)
        ax2.add_patch(wedge)
        ax2.text(i * 1.2, -0.7, '1/4', ha='center', fontsize=10, fontweight='bold')
        if i < 3:
            ax2.text((i + 0.5) * 1.2, 0, '+', ha='center', va='center', 
                    fontsize=14, fontweight='bold')
    
    ax2.text(4.8, 0, '=', ha='center', va='center', fontsize=14, fontweight='bold')
    circle2 = Circle((5.5, 0), 0.5, facecolor='#FFD700', 
                    edgecolor='black', linewidth=2)
    ax2.add_patch(circle2)
    ax2.text(5.5, -0.7, '1', ha='center', fontsize=10, fontweight='bold')
    
    # 2/4 = 1/2
    ax3 = axes[1, 0]
    ax3.set_aspect('equal')
    ax3.set_xlim(-2, 2)
    ax3.set_ylim(-1.5, 1.5)
    ax3.axis('off')
    ax3.set_title('2/4 is the same as 1/2!', fontsize=14, fontweight='bold')
    
    # Two quarters
    circle_left = Circle((-1, 0), 0.7, facecolor='white', 
                        edgecolor='black', linewidth=2)
    ax3.add_patch(circle_left)
    wedge_l1 = Wedge((-1, 0), 0.7, 0, 90, facecolor=colors[0], 
                    edgecolor='black', linewidth=2)
    ax3.add_patch(wedge_l1)
    wedge_l2 = Wedge((-1, 0), 0.7, 90, 180, facecolor=colors[0], 
                    edgecolor='black', linewidth=2)
    ax3.add_patch(wedge_l2)
    ax3.plot([-1, -1], [-0.7, 0.7], 'k-', linewidth=2)
    ax3.plot([-1.7, -0.3], [0, 0], 'k-', linewidth=2)
    ax3.text(-1, -1.1, '2/4', ha='center', fontsize=12, fontweight='bold')
    
    # Equals
    ax3.text(0, 0, '=', ha='center', va='center', fontsize=20, fontweight='bold')
    
    # One half
    circle_right = Circle((1, 0), 0.7, facecolor='white', 
                         edgecolor='black', linewidth=2)
    ax3.add_patch(circle_right)
    wedge_r = Wedge((1, 0), 0.7, 90, 270, facecolor=colors[0], 
                   edgecolor='black', linewidth=2)
    ax3.add_patch(wedge_r)
    ax3.plot([1, 1], [-0.7, 0.7], 'k-', linewidth=2)
    ax3.text(1, -1.1, '1/2', ha='center', fontsize=12, fontweight='bold')
    
    # Eating fractions
    ax4 = axes[1, 1]
    ax4.set_aspect('equal')
    ax4.set_xlim(-2, 2)
    ax4.set_ylim(-1.5, 1.5)
    ax4.axis('off')
    ax4.set_title('If you eat 1/4, what\'s left?', fontsize=14, fontweight='bold')
    
    # Whole with one quarter removed
    wedge_eaten = Wedge((0, 0), 1, 0, 90, facecolor='lightgray', 
                       edgecolor='black', linewidth=2, linestyle='--')
    ax4.add_patch(wedge_eaten)
    ax4.text(0.5, 0.5, 'Eaten!\n1/4', ha='center', va='center', 
            fontsize=10, color='gray')
    
    for i, (start, color) in enumerate(zip([90, 180, 270], [colors[1], colors[2], colors[3]])):
        wedge = Wedge((0, 0), 1, start, start + 90, facecolor=color, 
                     edgecolor='black', linewidth=2)
        ax4.add_patch(wedge)
    
    ax4.plot([-1, 1], [0, 0], 'k-', linewidth=2)
    ax4.plot([0, 0], [-1, 1], 'k-', linewidth=2)
    ax4.text(0, -1.3, 'Remaining: 3/4', ha='center', fontsize=12, fontweight='bold', color='green')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/04_fractions_adding.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/04_fractions_adding.png")
    plt.close()


def create_real_world_fractions():
    """
    Visualization 5: Real-world examples of halves and quarters
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Fractions in Real Life!', 
                fontsize=18, fontweight='bold', y=0.98)
    
    # Clock showing quarters
    ax1 = axes[0, 0]
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.axis('off')
    ax1.set_title('Clock: Quarter Hours', fontsize=14, fontweight='bold')
    
    # Clock circle
    circle = Circle((0, 0), 1, facecolor='white', 
                   edgecolor='black', linewidth=3)
    ax1.add_patch(circle)
    
    # Hour marks
    for hour in range(12):
        angle = np.pi / 2 - (hour * 30) * np.pi / 180
        x_outer = 0.9 * np.cos(angle)
        y_outer = 0.9 * np.sin(angle)
        x_inner = 0.8 * np.cos(angle)
        y_inner = 0.8 * np.sin(angle)
        ax1.plot([x_inner, x_outer], [y_inner, y_outer], 'k-', linewidth=2)
        
        # Labels for quarters
        if hour in [0, 3, 6, 9]:
            x_text = 1.2 * np.cos(angle)
            y_text = 1.2 * np.sin(angle)
            if hour == 0:
                ax1.text(x_text, y_text, ':00\n(Start)', ha='center', va='center', 
                        fontsize=10, fontweight='bold', color='red')
            elif hour == 3:
                ax1.text(x_text, y_text, ':15\n(1/4 hour)', ha='center', va='center', 
                        fontsize=10, fontweight='bold', color='blue')
            elif hour == 6:
                ax1.text(x_text, y_text, ':30\n(1/2 hour)', ha='center', va='center', 
                        fontsize=10, fontweight='bold', color='green')
            elif hour == 9:
                ax1.text(x_text, y_text, ':45\n(3/4 hour)', ha='center', va='center', 
                        fontsize=10, fontweight='bold', color='purple')
    
    # Money - quarters
    ax2 = axes[0, 1]
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 3)
    ax2.axis('off')
    ax2.set_title('Money: Quarters (25¢)', fontsize=14, fontweight='bold')
    
    # Draw 4 quarters
    for i in range(4):
        x = 0.7 + (i % 2) * 2
        y = 2 - (i // 2) * 1.2
        
        circle = Circle((x, y), 0.4, facecolor='silver', 
                       edgecolor='darkgray', linewidth=3)
        ax2.add_patch(circle)
        ax2.text(x, y, '25¢', ha='center', va='center', 
                fontsize=10, fontweight='bold')
        ax2.text(x, y - 0.6, f'Quarter {i+1}', ha='center', 
                fontsize=9, color='gray')
    
    ax2.text(2.5, 0.3, '4 quarters = $1.00 (1 dollar)', ha='center', 
            fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # Sports - game quarters
    ax3 = axes[1, 0]
    ax3.set_xlim(0, 5)
    ax3.set_ylim(0, 3)
    ax3.axis('off')
    ax3.set_title('Sports: Game Quarters', fontsize=14, fontweight='bold')
    
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    colors_q = [colors[0], colors[1], colors[2], colors[3]]
    
    for i, (q, color) in enumerate(zip(quarters, colors_q)):
        x = i * 1.2 + 0.7
        rect = Rectangle((x, 1.5), 1, 1, facecolor=color, 
                        edgecolor='black', linewidth=2)
        ax3.add_patch(rect)
        ax3.text(x + 0.5, 2, q, ha='center', va='center', 
                fontsize=16, fontweight='bold', color='white')
        ax3.text(x + 0.5, 1.2, '1/4 game', ha='center', 
                fontsize=9, fontweight='bold')
    
    ax3.text(2.5, 0.5, 'Each quarter = 1/4 of the game', ha='center', 
            fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # Recipe measuring cup
    ax4 = axes[1, 1]
    ax4.set_xlim(0, 3)
    ax4.set_ylim(0, 5)
    ax4.axis('off')
    ax4.set_title('Cooking: Measuring Cup', fontsize=14, fontweight='bold')
    
    # Draw measuring cup
    cup = Polygon([(0.7, 0.5), (0.5, 4), (2.5, 4), (2.3, 0.5)], 
                 facecolor='lightblue', alpha=0.3, edgecolor='black', linewidth=3)
    ax4.add_patch(cup)
    
    # Measurement lines
    measurements = [
        (0.5, '0 cups'),
        (1.375, '1/4 cup'),
        (2.25, '1/2 cup'),
        (3.125, '3/4 cup'),
        (4, '1 cup')
    ]
    
    for y, label in measurements:
        ax4.plot([0.5 + (y - 0.5) * 0.05, 2.5 - (y - 0.5) * 0.05], [y, y], 
                'k-', linewidth=2)
        ax4.text(2.7, y, label, ha='left', va='center', 
                fontsize=9, fontweight='bold')
    
    # Fill cup to 1/2
    fill = Polygon([(0.7, 0.5), (0.5 + (2.25 - 0.5) * 0.05, 2.25), 
                   (2.5 - (2.25 - 0.5) * 0.05, 2.25), (2.3, 0.5)], 
                  facecolor='lightblue', alpha=0.7, edgecolor='blue', linewidth=2)
    ax4.add_patch(fill)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/05_real_world_fractions.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/05_real_world_fractions.png")
    plt.close()


# Generate all visualizations
if __name__ == "__main__":
    print("Generating Fractions (Halves and Quarters) visualizations...")
    print("-" * 50)
    
    create_halves_shapes()
    create_quarters_shapes()
    create_half_vs_quarter_comparison()
    create_fractions_adding_up()
    create_real_world_fractions()
    
    print("-" * 50)
    print("✓ All visualizations generated successfully!")
    print(f"📁 Saved to: {output_dir}/")
