#!/usr/bin/env python3
"""
Generate markdown documentation from kits_catalog.yml

This script:
1. Reads kits/kits_catalog.yml
2. Generates kits/kits_catalog.md (comprehensive table)
3. Generates kits/kit_catalog_section.md (categorized sections for README)

Usage:
    python scripts/generate_kit_catalog.py
"""

import yaml
from pathlib import Path
from typing import List, Dict


def load_catalog(yaml_path: Path) -> List[Dict]:
    """Load kits from YAML catalog."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('kits', [])


def categorize_kit(kit: Dict) -> str:
    """Categorize kit by difficulty level."""
    difficulty = kit.get('Difficulty', '').lower()
    
    if difficulty in ['low', 'low-medium']:
        return 'Easy'
    elif difficulty in ['medium', 'medium-high']:
        return 'Medium'
    elif difficulty in ['high']:
        return 'Advanced'
    else:
        return 'Medium'  # Default


def generate_markdown_table(kits: List[Dict]) -> str:
    """Generate a comprehensive markdown table of all kits."""
    lines = []
    lines.append("# Power Electronics Evaluation Kits Catalog")
    lines.append("")
    lines.append("Complete list of evaluation boards in this repository.")
    lines.append("")
    
    # Table header
    lines.append("| ID | Vendor | Kit Part Number | Topology | Isolated | Power | Difficulty | Application |")
    lines.append("|----|--------|-----------------|----------|----------|-------|------------|-------------|")
    
    # Table rows
    for kit in kits:
        kit_id = kit.get('ID', '')
        vendor = kit.get('Vendor', '')
        part_num = kit.get('Kit Part Number', '')
        topology = kit.get('Topology', '')
        isolated = kit.get('Isolated (Yes/No)', '')
        power = kit.get('Pout Range', '')
        difficulty = kit.get('Difficulty', '')
        application = kit.get('Application Domain', '')
        
        # Create link if analysis exists
        link_to_analysis = kit.get('Link to Analysis', '').strip()
        if link_to_analysis:
            part_num = f"[{part_num}]({link_to_analysis})"
        
        lines.append(f"| {kit_id} | {vendor} | {part_num} | {topology} | {isolated} | {power} | {difficulty} | {application} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated from `kits_catalog.yml`*")
    lines.append("")
    
    return '\n'.join(lines)


def generate_catalog_section(kits: List[Dict]) -> str:
    """Generate categorized catalog section for README."""
    lines = []
    lines.append("## Kit Catalog")
    lines.append("")
    lines.append("Browse available evaluation boards in `kits/`. See [kits/kits_catalog.md](kits/kits_catalog.md) for the complete table.")
    lines.append("")
    
    # Group kits by difficulty
    categories = {
        'Easy': [],
        'Medium': [],
        'Advanced': []
    }
    
    for kit in kits:
        category = categorize_kit(kit)
        categories[category].append(kit)
    
    # Easy kits
    if categories['Easy']:
        lines.append("### Easy (Entry-Level)")
        lines.append("")
        lines.append("Non-isolated DC/DC and low-power offline boards.")
        lines.append("")
        
        for kit in categories['Easy']:
            vendor = kit.get('Vendor', '')
            part_num = kit.get('Kit Part Number', '')
            topology = kit.get('Topology', '').lower()
            vin = kit.get('Vin Range', '')
            vout = kit.get('Vout Range', '')
            power = kit.get('Pout Range', '')
            link = kit.get('Link to Analysis', '').strip()
            
            # Format the line
            if link:
                kit_name = f"**[{part_num}]({link})**"
            else:
                kit_name = f"**{part_num}**"
            
            # Create description
            desc_parts = [topology]
            if vin and vout:
                desc_parts.append(f"{vin} → {vout}")
            elif vin:
                desc_parts.append(f"{vin} in")
            if power:
                desc_parts.append(power)
            
            description = ', '.join(desc_parts)
            lines.append(f"- {kit_name} · {description}")
        
        lines.append("")
    
    # Medium kits
    if categories['Medium']:
        lines.append("### Medium")
        lines.append("")
        lines.append("Intermediate power, more complex control or wide-VIN.")
        lines.append("")
        
        for kit in categories['Medium']:
            vendor = kit.get('Vendor', '')
            part_num = kit.get('Kit Part Number', '')
            topology = kit.get('Topology', '').lower()
            vin = kit.get('Vin Range', '')
            vout = kit.get('Vout Range', '')
            power = kit.get('Pout Range', '')
            link = kit.get('Link to Analysis', '').strip()
            
            if link:
                kit_name = f"**[{part_num}]({link})**"
            else:
                kit_name = f"**{part_num}**"
            
            desc_parts = [topology]
            if vin and vout:
                desc_parts.append(f"{vin} → {vout}")
            elif vin:
                desc_parts.append(f"{vin} in")
            if power:
                desc_parts.append(power)
            
            description = ', '.join(desc_parts)
            lines.append(f"- {kit_name} · {description}")
        
        lines.append("")
    
    # Advanced kits
    if categories['Advanced']:
        lines.append("### Advanced / High Power")
        lines.append("")
        lines.append("kW-class boards with complex topologies (LLC, PSFB, bidirectional, PFC+LLC).")
        lines.append("")
        
        for kit in categories['Advanced']:
            vendor = kit.get('Vendor', '')
            part_num = kit.get('Kit Part Number', '')
            topology = kit.get('Topology', '').lower()
            vin = kit.get('Vin Range', '')
            vout = kit.get('Vout Range', '')
            power = kit.get('Pout Range', '')
            link = kit.get('Link to Analysis', '').strip()
            
            if link:
                kit_name = f"**[{part_num}]({link})**"
            else:
                kit_name = f"**{part_num}**"
            
            desc_parts = [topology]
            if vin and vout:
                desc_parts.append(f"{vin} → {vout}")
            elif vin:
                desc_parts.append(f"{vin} in")
            if power:
                desc_parts.append(power)
            
            description = ', '.join(desc_parts)
            lines.append(f"- {kit_name} · {description}")
        
        lines.append("")
    
    lines.append("> **Note:** Not all kits have folders yet. Contributions welcome! Use [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md) to add one.")
    lines.append("")
    
    return '\n'.join(lines)


def insert_into_readme(section_path: Path, readme_path: Path) -> bool:
    """Insert catalog section into README.md."""
    import re
    
    # Read the catalog section
    with open(section_path, 'r', encoding='utf-8') as f:
        catalog_content = f.read().strip()
    
    # Read the README
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Pattern to match Kit Catalog section
    pattern = r'(---\s*\n\s*)## Kit Catalog.*?(?=\n---|\n## |\Z)'
    
    # Create replacement
    replacement = r'\1' + catalog_content + '\n\n'
    
    # Perform replacement
    new_content, count = re.subn(pattern, replacement, readme_content, flags=re.DOTALL)
    
    if count == 0:
        return False
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    """Main execution function."""
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    yaml_path = repo_root / 'kits' / 'kits_catalog.yml'
    table_output = repo_root / 'kits' / 'kits_catalog.md'
    section_output = repo_root / 'kits' / 'kit_catalog_section.md'
    readme_path = repo_root / 'README.md'
    
    print(f"Reading catalog from: {yaml_path}")
    
    # Load kits
    kits = load_catalog(yaml_path)
    print(f"Loaded {len(kits)} kits")
    
    # Generate markdown table
    print("Generating markdown table...")
    table_md = generate_markdown_table(kits)
    with open(table_output, 'w', encoding='utf-8') as f:
        f.write(table_md)
    print(f"Written: {table_output}")
    
    # Generate catalog section
    print("Generating catalog section...")
    section_md = generate_catalog_section(kits)
    with open(section_output, 'w', encoding='utf-8') as f:
        f.write(section_md)
    print(f"Written: {section_output}")
    
    # Insert into README
    print("Updating README.md...")
    if insert_into_readme(section_output, readme_path):
        print(f"Updated: {readme_path}")
    else:
        print("Warning: Could not find Kit Catalog section in README.md")
    
    print("\nDone! Generated files:")
    print(f"  - Full table: {table_output.relative_to(repo_root)}")
    print(f"  - Section: {section_output.relative_to(repo_root)}")
    print(f"  - Updated: {readme_path.relative_to(repo_root)}")


if __name__ == '__main__':
    main()
