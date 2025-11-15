#!/bin/bash
# Update kit catalog from YAML
# Usage: ./scripts/update_catalog.sh

echo "Updating kit catalog from YAML..."
python scripts/generate_kit_catalog.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Success! Generated and updated:"
    echo "  - kits/kits_catalog.md (complete table)"
    echo "  - kits/kit_catalog_section.md (section content)"
    echo "  - README.md (Kit Catalog section)"
    echo ""
    echo "Kit catalog is up to date!"
else
    echo ""
    echo "Error: Script failed with exit code $?"
    exit $?
fi
