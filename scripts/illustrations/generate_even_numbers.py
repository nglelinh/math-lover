#!/usr/bin/env python3
"""
Generate visualizations for Even Numbers lesson (Chapter 01)
Demonstrates the pattern of even numbers and pairing concept
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
import os

# Create output directory if it doesn't exist
output_dir = "../../img/chapter_img/chapter01"
os.makedirs(output_dir, exist_ok=True)

# Set style for child-friendly visuals
plt.style.use('seaborn-v0_8-bright')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

def create_even_number_pattern():
    """
    Visualization 1: Even numbers on a number line showing the pattern
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Number range
    numbers = np.arange(1, 21)
    even_nums = numbers[numbers % 2 == 0]
    odd_nums = numbers[numbers % 2 == 1]
    
    # Plot odd numbers (smaller, gray)
    ax.scatter(odd_nums, [1]*len(odd_nums), s=300, c='lightgray', 
               alpha=0.5, edgecolors='gray', linewidth=2, zorder=2)
    
    # Plot even numbers (larger, colorful)
    ax.scatter(even_nums, [1]*len(even_nums), s=500, c=colors[0], 
               alpha=0.9, edgecolors='darkred', linewidth=3, zorder=3)
    
    # Label each number
    for num in numbers:
        if num % 2 == 0:
            ax.text(num, 1, str(num), ha='center', va='center', 
                   fontsize=14, fontweight='bold', color='white')
        else:
            ax.text(num, 1, str(num), ha='center', va='center', 
                   fontsize=10, color='gray')
    
    # Add title and labels
    ax.set_title('Even Numbers Pattern: 2, 4, 6, 8, 10, ...', 
                fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Numbers', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 21)
    ax.set_ylim(0.5, 1.5)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add legend
    legend_text = "Red circles = EVEN numbers (can split into 2 equal groups)\n" \
                  "Gray circles = ODD numbers (always have 1 left over)"
    ax.text(10.5, 0.65, legend_text, ha='center', fontsize=11, 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/01_even_number_pattern.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/01_even_number_pattern.png")
    plt.close()


def create_pairing_visualization():
    """
    Visualization 2: Show even numbers as pairs of objects
    """
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle('Even Numbers Split into Perfect Pairs', 
                fontsize=18, fontweight='bold', y=0.98)
    
    even_numbers = [2, 4, 6, 8, 10, 12]
    
    for idx, (ax, num) in enumerate(zip(axes.flat, even_numbers)):
        pairs = num // 2
        
        # Draw pairs of circles
        x_positions = []
        y_positions = []
        
        for pair in range(pairs):
            # Two circles per pair
            x1 = pair * 2.5 + 0.5
            x2 = pair * 2.5 + 1.5
            x_positions.extend([x1, x2])
            y_positions.extend([1, 1])
        
        # Draw circles
        for x, y in zip(x_positions, y_positions):
            circle = Circle((x, y), 0.4, color=colors[idx % len(colors)], 
                          ec='black', linewidth=2)
            ax.add_patch(circle)
        
        # Draw grouping boxes around pairs
        for pair in range(pairs):
            rect = Rectangle((pair * 2.5 + 0.05, 0.5), 1.9, 1.0, 
                           fill=False, edgecolor='black', 
                           linewidth=2, linestyle='--')
            ax.add_patch(rect)
        
        # Set up axes
        ax.set_xlim(-0.5, max(6, pairs * 2.5 + 1))
        ax.set_ylim(0, 2)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Add title
        ax.text(pairs * 1.25, 0.2, f'{num} = {pairs} pairs', 
               ha='center', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/02_even_pairs.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/02_even_pairs.png")
    plt.close()


def create_even_vs_odd_comparison():
    """
    Visualization 3: Compare even and odd numbers side by side
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Even numbers visualization
    even_examples = [4, 6, 8]
    ax1.set_title('EVEN Numbers: Split Perfectly into 2 Equal Groups', 
                 fontsize=16, fontweight='bold', color='darkgreen')
    
    for idx, num in enumerate(even_examples):
        y_base = 3 - idx
        per_group = num // 2
        
        # Left group
        for i in range(per_group):
            circle = Circle((i + 1, y_base), 0.3, color=colors[0], 
                          ec='black', linewidth=2)
            ax1.add_patch(circle)
        
        # Right group
        for i in range(per_group):
            circle = Circle((i + 6, y_base), 0.3, color=colors[1], 
                          ec='black', linewidth=2)
            ax1.add_patch(circle)
        
        # Add label
        ax1.text(3.5, y_base, f'{num} ÷ 2', ha='center', va='center', 
                fontsize=12, fontweight='bold')
        ax1.text(0, y_base, f'{per_group}', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkgreen')
        ax1.text(7, y_base, f'{per_group}', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkgreen')
    
    ax1.set_xlim(-1, 9)
    ax1.set_ylim(0, 4)
    ax1.axis('off')
    ax1.text(4, 0.3, '✓ Perfect split! No leftovers!', ha='center', 
            fontsize=14, fontweight='bold', color='darkgreen',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # Odd numbers visualization
    odd_examples = [3, 5, 7]
    ax2.set_title('ODD Numbers: Always Have 1 Left Over', 
                 fontsize=16, fontweight='bold', color='darkred')
    
    for idx, num in enumerate(odd_examples):
        y_base = 3 - idx
        per_group = num // 2
        
        # Left group
        for i in range(per_group):
            circle = Circle((i + 1, y_base), 0.3, color=colors[2], 
                          ec='black', linewidth=2)
            ax2.add_patch(circle)
        
        # Right group
        for i in range(per_group):
            circle = Circle((i + 5.5, y_base), 0.3, color=colors[3], 
                          ec='black', linewidth=2)
            ax2.add_patch(circle)
        
        # Leftover (the odd one out!)
        circle = Circle((3.5, y_base), 0.3, color='gold', 
                      ec='red', linewidth=3)
        ax2.add_patch(circle)
        ax2.text(3.5, y_base - 0.6, '← Leftover!', ha='center', 
                fontsize=10, color='red', fontweight='bold')
        
        # Add label
        ax2.text(0, y_base, f'{per_group}', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkred')
        ax2.text(6.5, y_base, f'{per_group}', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkred')
    
    ax2.set_xlim(-1, 9)
    ax2.set_ylim(0, 4)
    ax2.axis('off')
    ax2.text(4, 0.3, '✗ Not equal! One is always left over!', ha='center', 
            fontsize=14, fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/03_even_vs_odd.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/03_even_vs_odd.png")
    plt.close()


def create_double_pattern():
    """
    Visualization 4: Show even numbers as doubles (for extension activity)
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title('Even Numbers Are Doubles!', fontsize=18, fontweight='bold')
    
    numbers = np.arange(1, 11)
    doubles = numbers * 2
    
    # Create bar chart showing the doubling pattern
    bars = ax.bar(numbers, doubles, color=colors[0], alpha=0.8, 
                  edgecolor='black', linewidth=2)
    
    # Add value labels on bars
    for i, (num, double) in enumerate(zip(numbers, doubles)):
        ax.text(num, double + 0.5, f'{double}', ha='center', 
               fontsize=12, fontweight='bold')
        ax.text(num, -1.5, f'{num}', ha='center', 
               fontsize=10, color='blue', fontweight='bold')
    
    # Add arrows and annotations
    ax.annotate('', xy=(5, 10), xytext=(5, 5),
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax.text(5.5, 7.5, 'Double!', fontsize=14, fontweight='bold', color='red')
    
    ax.set_xlabel('Original Number (n)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Double (2 × n)', fontsize=14, fontweight='bold')
    ax.set_xticks(numbers)
    ax.set_ylim(-3, 22)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add pattern explanation
    ax.text(5.5, 18, 'Pattern: Even Number = 2 × (some number)', 
           ha='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/04_double_pattern.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/04_double_pattern.png")
    plt.close()


# Generate all visualizations
if __name__ == "__main__":
    print("Generating Even Numbers visualizations...")
    print("-" * 50)
    
    create_even_number_pattern()
    create_pairing_visualization()
    create_even_vs_odd_comparison()
    create_double_pattern()
    
    print("-" * 50)
    print("✓ All visualizations generated successfully!")
    print(f"📁 Saved to: {output_dir}/")
