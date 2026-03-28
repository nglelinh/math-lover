#!/usr/bin/env python3
"""
Generate visualizations for Skip Counting by 2s lesson (Chapter 02)
Demonstrates skip counting patterns, number line jumps, and multiplication connection
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch
import os

# Create output directory if it doesn't exist
output_dir = "../../img/chapter_img/chapter02"
os.makedirs(output_dir, exist_ok=True)

# Set style for child-friendly visuals
plt.style.use('seaborn-v0_8-bright')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F38181', '#95E1D3']

def create_number_line_jumps():
    """
    Visualization 1: Number line with skip counting jumps
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Draw number line
    numbers = np.arange(0, 21)
    
    # Draw base line
    ax.plot([0, 20], [0, 0], 'k-', linewidth=3)
    
    # Add tick marks for all numbers
    for num in numbers:
        if num % 2 == 0:
            ax.plot([num, num], [-0.3, 0.3], 'k-', linewidth=3)
            ax.text(num, -0.8, str(num), ha='center', va='top', 
                   fontsize=14, fontweight='bold', color='darkblue')
        else:
            ax.plot([num, num], [-0.15, 0.15], 'gray', linewidth=1, alpha=0.5)
            ax.text(num, -0.8, str(num), ha='center', va='top', 
                   fontsize=10, color='gray', alpha=0.6)
    
    # Draw jumps (arcs) for skip counting
    skip_count_nums = np.arange(0, 21, 2)
    for i in range(len(skip_count_nums) - 1):
        start = skip_count_nums[i]
        end = skip_count_nums[i + 1]
        
        # Create curved arrow
        arrow = FancyArrowPatch((start, 0.1), (end, 0.1),
                               connectionstyle="arc3,rad=.5", 
                               arrowstyle='->', 
                               mutation_scale=30, 
                               linewidth=3,
                               color=colors[i % len(colors)])
        ax.add_patch(arrow)
        
        # Add "+2" label on each jump
        mid_point = (start + end) / 2
        ax.text(mid_point, 1.3, '+2', ha='center', va='bottom', 
               fontsize=11, fontweight='bold', color=colors[i % len(colors)])
    
    ax.set_title('Skip Counting by 2s: Jump +2 Each Time!', 
                fontsize=18, fontweight='bold', pad=20)
    ax.set_xlim(-1, 21)
    ax.set_ylim(-2, 2.5)
    ax.axis('off')
    
    # Add instruction box
    instruction = "Start at 0, jump forward 2 spaces each time!\n" \
                 "We only land on EVEN numbers: 0, 2, 4, 6, 8, 10, ..."
    ax.text(10, -1.5, instruction, ha='center', fontsize=12, 
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/01_number_line_jumps.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/01_number_line_jumps.png")
    plt.close()


def create_towers_of_two():
    """
    Visualization 2: Towers of 2 objects showing skip counting
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    
    num_towers = 10
    ax.set_title('Counting Towers of 2', fontsize=18, fontweight='bold', pad=20)
    
    for tower in range(num_towers):
        x_pos = tower * 1.5 + 1
        
        # Draw two circles stacked
        for height in range(2):
            circle = Circle((x_pos, height + 1), 0.35, 
                          color=colors[tower % len(colors)], 
                          ec='black', linewidth=2)
            ax.add_patch(circle)
        
        # Add count below
        total = (tower + 1) * 2
        ax.text(x_pos, 0.2, str(total), ha='center', va='top', 
               fontsize=14, fontweight='bold', color='darkblue')
        
        # Add tower number
        ax.text(x_pos, -0.3, f'Tower {tower + 1}', ha='center', va='top', 
               fontsize=9, color='gray')
    
    ax.set_xlim(0, num_towers * 1.5 + 1)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    
    # Add counting sequence
    sequence = "2, 4, 6, 8, 10, 12, 14, 16, 18, 20"
    ax.text(num_towers * 0.75, 3.5, f'Skip count: {sequence}', 
           ha='center', fontsize=14, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/02_towers_of_two.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/02_towers_of_two.png")
    plt.close()


def create_socks_pairs():
    """
    Visualization 3: Counting socks in pairs (real-world example)
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_title('Counting Socks by Pairs (Skip Counting by 2s)', 
                fontsize=18, fontweight='bold', pad=20)
    
    num_pairs = 7
    
    for pair in range(num_pairs):
        y_pos = 7 - pair
        
        # Draw two socks
        for sock in range(2):
            x_pos = 1.5 + sock * 1.2
            
            # Sock body (rectangle)
            sock_rect = Rectangle((x_pos, y_pos - 0.4), 0.8, 1.2, 
                                  color=colors[pair % len(colors)], 
                                  ec='black', linewidth=2)
            ax.add_patch(sock_rect)
            
            # Sock toe (circle)
            toe_circle = Circle((x_pos + 0.4, y_pos - 0.5), 0.15, 
                              color=colors[pair % len(colors)], 
                              ec='black', linewidth=2)
            ax.add_patch(toe_circle)
        
        # Draw bracket showing the pair
        ax.plot([3.8, 3.8], [y_pos - 0.5, y_pos + 0.7], 'k-', linewidth=2)
        ax.plot([3.8, 4.0], [y_pos - 0.5, y_pos - 0.5], 'k-', linewidth=2)
        ax.plot([3.8, 4.0], [y_pos + 0.7, y_pos + 0.7], 'k-', linewidth=2)
        
        # Add count
        total = (pair + 1) * 2
        ax.text(4.5, y_pos + 0.1, f'Pair {pair + 1} → {total} socks total', 
               ha='left', va='center', fontsize=13, fontweight='bold')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Add summary
    summary = "7 pairs of socks = 14 socks\n" \
             "Skip counted by 2s seven times: 2, 4, 6, 8, 10, 12, 14"
    ax.text(5, 0.5, summary, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/03_socks_pairs.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/03_socks_pairs.png")
    plt.close()


def create_skip_count_pattern():
    """
    Visualization 4: Visual pattern showing skip counting sequence
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Create a grid showing skip counting
    skip_nums = np.arange(2, 31, 2)
    
    # Arrange in rows of 5
    rows = 3
    cols = 5
    
    ax.set_title('Skip Counting by 2s Pattern', 
                fontsize=18, fontweight='bold', pad=20)
    
    for idx, num in enumerate(skip_nums):
        row = idx // cols
        col = idx % cols
        
        x = col * 2 + 1
        y = 2 * (rows - row)
        
        # Draw fancy box
        box = FancyBboxPatch((x - 0.7, y - 0.5), 1.4, 1.0,
                            boxstyle="round,pad=0.1", 
                            facecolor=colors[idx % len(colors)],
                            edgecolor='black', linewidth=3)
        ax.add_patch(box)
        
        # Add number
        ax.text(x, y, str(num), ha='center', va='center', 
               fontsize=18, fontweight='bold', color='white')
        
        # Add arrow to next number (except last in row)
        if col < cols - 1 and idx < len(skip_nums) - 1:
            ax.annotate('', xy=(x + 1.3, y), xytext=(x + 0.7, y),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
            ax.text(x + 1, y + 0.6, '+2', ha='center', va='bottom', 
                   fontsize=10, fontweight='bold')
    
    ax.set_xlim(-0.5, cols * 2 + 0.5)
    ax.set_ylim(0, rows * 2 + 1)
    ax.axis('off')
    
    # Add pattern observation
    observation = "Pattern: Start at 2, add 2 each time\n" \
                 "All numbers end in 0, 2, 4, 6, or 8"
    ax.text(5, 0.3, observation, ha='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/04_skip_count_pattern.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/04_skip_count_pattern.png")
    plt.close()


def create_multiplication_connection():
    """
    Visualization 5: Show connection between skip counting and multiplication
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title('Skip Counting by 2s = Multiplication by 2!', 
                fontsize=18, fontweight='bold', pad=20)
    
    numbers = np.arange(1, 11)
    
    for i, n in enumerate(numbers):
        y_pos = 10 - i
        
        # Draw groups of 2
        result = n * 2
        for group in range(n):
            x_base = group * 0.6
            for item in range(2):
                circle = Circle((x_base, y_pos + item * 0.3 - 0.15), 0.1, 
                              color=colors[i % len(colors)], 
                              ec='black', linewidth=1)
                ax.add_patch(circle)
        
        # Add equation
        eq_text = f'{n} groups of 2  =  {n} × 2  =  {result}'
        ax.text(7, y_pos, eq_text, ha='left', va='center', 
               fontsize=12, fontweight='bold')
        
        # Add skip counting sequence
        skip_sequence = ', '.join(str(x * 2) for x in range(1, n + 1))
        ax.text(12, y_pos, skip_sequence, ha='left', va='center', 
               fontsize=10, color='blue')
    
    ax.set_xlim(-0.5, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    # Add key insight
    insight = "🔍 Pattern Discovery: Skip counting by 2s is the same as multiplying by 2!"
    ax.text(8, 0.5, insight, ha='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='gold', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/05_multiplication_connection.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/05_multiplication_connection.png")
    plt.close()


# Generate all visualizations
if __name__ == "__main__":
    print("Generating Skip Counting by 2s visualizations...")
    print("-" * 50)
    
    create_number_line_jumps()
    create_towers_of_two()
    create_socks_pairs()
    create_skip_count_pattern()
    create_multiplication_connection()
    
    print("-" * 50)
    print("✓ All visualizations generated successfully!")
    print(f"📁 Saved to: {output_dir}/")
