# Illustration Generation Scripts

This directory contains Python scripts to generate mathematical visualizations for the Math-Lover course.

## Requirements

```bash
pip install matplotlib numpy
```

Or if using the project's requirements:

```bash
pip install -r requirements.txt
```

## Available Scripts

### 1. `generate_even_numbers.py`

Generates visualizations for Chapter 01 (Discovering Even Numbers):

```bash
python3 generate_even_numbers.py
```

**Outputs:**
- `01_even_number_pattern.png` - Number line highlighting even numbers
- `02_even_pairs.png` - Visual representation of pairing
- `03_even_vs_odd.png` - Side-by-side comparison
- `04_double_pattern.png` - Doubling pattern visualization

### 2. `generate_skip_counting.py`

Generates visualizations for Chapter 02 (Skip Counting by 2s):

```bash
python3 generate_skip_counting.py
```

**Outputs:**
- `01_number_line_jumps.png` - Animated jump pattern on number line
- `02_towers_of_two.png` - Stacked objects showing counting
- `03_socks_pairs.png` - Real-world socks example
- `04_skip_count_pattern.png` - Grid pattern visualization
- `05_multiplication_connection.png` - Link to multiplication

### 3. `generate_fractions.py`

Generates visualizations for Chapter 04 (Halves and Quarters):

```bash
python3 generate_fractions.py
```

**Outputs:**
- `01_halves_shapes.png` - Various shapes divided into halves
- `02_quarters_shapes.png` - Various shapes divided into quarters
- `03_half_vs_quarter.png` - Size comparison
- `04_fractions_adding.png` - Adding fractions to make wholes
- `05_real_world_fractions.png` - Real-world applications

### 4. `generate_chapter03.py`

Generates static illustrations for Chapter 03 core lessons:

```bash
python3 generate_chapter03.py
```

**Outputs:**
- `03_01_toan_tu_duy.png` - Logic elimination puzzle
- `03_02_dien_tich_nang_cao.png` - Area by cutting and joining
- `03_03_so_lon.png` - Place value ladder
- `03_04_bai_toan_do.png` - Word-problem solving flow
- `03_05_tam_giac_pascal.png` - Pascal triangle pattern
- `03_06_luoi_so.png` - Grid and Sudoku logic
- `03_07_tim_quy_luat.png` - Pattern examples
- `03_08_toan_vui.png` - Math games overview
- `03_09_fibonacci.png` - Fibonacci growth pattern
- `03_10_on_tap.png` - Chapter review map

### 5. `generate_chapter05.py`

Generates static illustrations for Chapter 05 core lessons:

```bash
python3 generate_chapter05.py
```

**Outputs:**
- `01_square_numbers.png` - Square-number dot arrays
- `02_factors_multiples.png` - Factors and multiples map
- `03_prime_numbers.png` - Prime-number highlight chart
- `04_gcf.png` - Greatest common factor overlap
- `05_lcm.png` - Least common multiple rows
- `06_equivalent_fractions.png` - Equivalent fraction bars
- `07_comparing_fractions.png` - Fraction comparison bars
- `08_add_subtract_fractions.png` - Add/subtract fraction visuals
- `09_mixed_numbers.png` - Mixed-number model
- `10_chapter5_review.png` - Chapter review concept map

### 6. `generate_chapter02_vi.py`

Generates static illustrations for Vietnamese Chapter 02 core lessons:

```bash
python3 generate_chapter02_vi.py
```

**Outputs:**
- `02_01_so_nguyen_to.png` - Prime-number chart
- `02_02_ucln_bcnn.png` - GCF and LCM comparison
- `02_03_nhan_nhanh.png` - Quick multiplication patterns
- `02_04_chia_nhanh.png` - Equal-group division model
- `02_05_tinh_chat.png` - Operation properties cards
- `02_06_phan_so_nang_cao.png` - Fraction comparison and sum
- `02_07_so_thap_phan.png` - Decimals on a number line
- `02_08_ti_le_phan_tram.png` - Percent as a 100-grid
- `02_09_goc_duong_thang.png` - Angles and lines overview
- `02_10_on_tap_kiem_tra.png` - Chapter review map

### 7. `generate_chapter06.py`

Generates static illustrations for Chapter 06 core lessons:

```bash
python3 generate_chapter06.py
```

**Outputs:**
- `01_decimal_numbers.png` - Decimal number line and place values
- `02_add_subtract_decimals.png` - Decimal addition and subtraction
- `03_multiply_divide_decimals.png` - Decimal shift patterns
- `04_ratios_proportions.png` - Ratios and proportions overview
- `05_direct_inverse_proportion.png` - Direct vs inverse graphs
- `06_rectangle_parallelogram.png` - Rectangle and parallelogram shapes
- `07_rhombus_trapezoid.png` - Rhombus and trapezoid shapes
- `08_area_circle_triangle.png` - Triangle and circle area models
- `09_volume.png` - Prism and cube volume models
- `10_chapter6_review.png` - Chapter review concept map

### 8. `generate_chapter07.py`

Generates static illustrations for Chapter 07 core lessons:

```bash
python3 generate_chapter07.py
```

**Outputs:**
- `01_probability.png` - Coin and dice probability models
- `02_statistics.png` - Mean, median, and mode snapshot
- `03_charts.png` - Bar, line, and pie chart examples
- `04_equations.png` - Step-by-step equation solving
- `05_percent.png` - Percent in daily-life pricing
- `06_sphere_cone.png` - Sphere and cone models
- `07_cylinder.png` - Cylinder volume model
- `08_sequences.png` - Additive and multiplicative sequences
- `09_binary.png` - Binary place-value grid
- `10_chapter7_review.png` - Chapter review concept map

### 9. `generate_chapter04_vi.py`

Generates static illustrations for Vietnamese Chapter 04 lessons:

```bash
python3 generate_chapter04_vi.py
```

**Outputs:**
- `04_01_dai_so_bien_so.png` - Variable cards
- `04_02_phuong_trinh.png` - Equation-solving steps
- `04_03_phan_so_thap_phan.png` - Fractions and decimals bridge
- `04_04_ty_le_thuan_nghich.png` - Direct and inverse relationships
- `04_05_phan_tram_ung_dung.png` - Percent applications
- `04_06_hinh_hoc_hinh_tam_giac_hinh_vuong.png` - Triangle and square overview
- `04_07_do_luong_don_vi_do_dai_khoi_luong.png` - Measurement units map
- `04_08_thoi_gian_xem_dong_ho_va_lich.png` - Clock and calendar
- `04_09_du_lieu_thu_thap_va_bieu_dien_thong_tin.png` - Data bar chart
- `04_10_on_tap_tong_ket_chuong_4.png` - Chapter review concept map

## Regenerating All Visualizations

To regenerate all visualizations at once:

```bash
python3 generate_even_numbers.py && \
python3 generate_skip_counting.py && \
python3 generate_fractions.py && \
python3 generate_chapter03.py && \
python3 generate_chapter05.py && \
python3 generate_chapter02_vi.py && \
python3 generate_chapter06.py && \
python3 generate_chapter07.py && \
python3 generate_chapter04_vi.py
```

## Output Directories

Images are saved to:
- `../../img/chapter_img/chapter01/` (Even Numbers)
- `../../img/chapter_img/chapter02/` (Skip Counting)
- `../../img/chapter_img/chapter04/` (Fractions)
- `../../img/chapter_img/chapter03/` (Logic, patterns, and review)
- `../../img/chapter_img/chapter05/` (Number relationships and fractions)
- `../../img/chapter_img/chapter02/` (Vietnamese core lessons)
- `../../img/chapter_img/chapter06/` (Decimals, ratios, geometry, and volume)
- `../../img/chapter_img/chapter07/` (Probability, data, equations, and 3D shapes)
- `../../img/chapter_img/chapter04/` (Vietnamese fractions, review, and legacy lessons)

## Customization

### Changing Colors

Each script has a `colors` array near the top. Modify hex codes to change the color scheme:

```python
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
```

### Adjusting Figure Sizes

Modify the `figsize` parameter in `plt.subplots()`:

```python
fig, ax = plt.subplots(figsize=(12, 6))  # width=12, height=6 inches
```

### Changing DPI (Image Quality)

Higher DPI = higher quality but larger file size:

```python
plt.savefig(f'{output_dir}/filename.png', dpi=150)  # Change 150 to 200 or 300
```

## Script Structure

Each script follows this pattern:

```python
#!/usr/bin/env python3
"""
Script description
"""

import matplotlib.pyplot as plt
import numpy as np
# ... other imports

# Setup
output_dir = "../../img/chapter_img/chapterXX"
colors = [...]

def create_visualization_1():
    """Docstring explaining what this creates"""
    # Create figure
    # Draw visualization
    # Save to file
    
def create_visualization_2():
    # ... more visualizations

if __name__ == "__main__":
    create_visualization_1()
    create_visualization_2()
    # ...
```

## Best Practices

1. **Keep it simple** - Child-friendly visuals should be clear and uncluttered
2. **Use bright colors** - Make it engaging for children aged 8+
3. **Label clearly** - Add titles, axis labels, and explanatory text
4. **Test readability** - View at different sizes to ensure text is readable
5. **Comment your code** - Explain what each section does

## Creating New Visualizations

To create visualizations for a new chapter:

1. Copy an existing script (e.g., `generate_even_numbers.py`)
2. Rename it (e.g., `generate_chapter05.py`)
3. Update the `output_dir` variable
4. Create new visualization functions
5. Update the main section to call your functions
6. Run and test!

Example template:

```python
#!/usr/bin/env python3
"""
Generate visualizations for Chapter XX: [Topic Name]
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
output_dir = "../../img/chapter_img/chapterXX"
os.makedirs(output_dir, exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-bright')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

def create_my_visualization():
    """
    Description of what this creates
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Your visualization code here
    
    plt.savefig(f'{output_dir}/01_my_visualization.png', dpi=150, bbox_inches='tight')
    print(f"✓ Created: {output_dir}/01_my_visualization.png")
    plt.close()

if __name__ == "__main__":
    print("Generating Chapter XX visualizations...")
    print("-" * 50)
    
    create_my_visualization()
    
    print("-" * 50)
    print("✓ All visualizations generated successfully!")
    print(f"📁 Saved to: {output_dir}/")
```

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`:

```bash
pip install matplotlib numpy
```

### Font Warnings

Matplotlib may warn about missing glyphs (like emojis). This is safe to ignore - the images will still generate correctly.

### Permission Errors

Ensure the output directories exist and are writable:

```bash
mkdir -p ../../img/chapter_img/chapter01
```

### Memory Issues

If generating many large images causes memory issues, add `plt.close()` after each save:

```python
plt.savefig('image.png')
plt.close()  # Free memory
```

## Mathematical Libraries Used

- **matplotlib** - Plotting and visualization
- **numpy** - Numerical operations and arrays
- **matplotlib.patches** - Geometric shapes (circles, rectangles, polygons)

## Additional Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Examples and inspiration

## Future Enhancements

Ideas for expanding the illustration system:

- [ ] Animated GIFs for showing processes step-by-step
- [ ] 3D visualizations for geometry lessons
- [ ] Interactive plots using Plotly or Bokeh
- [ ] SVG output for resolution-independent graphics
- [ ] Batch processing script to regenerate all chapters
- [ ] Configuration file for colors/styles across all chapters
- [ ] Command-line arguments for customization

## Contact

For questions or suggestions about the visualization scripts, please see the main project README.

---

**Happy visualizing!** 📊🎨
