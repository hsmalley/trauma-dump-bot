#!/bin/bash

# Clean up mac stuff
find . -type f -name .DS_Store -delete
# Export Vault as json but leave data out of it #
python3 ./tools/vault_to_json.py --root . --out .Relational_Analysis_Vault.json --exclude-tag-all=.tar_exclude.tag
# Clean up the stuff, including json files
prettier --cache --cache-location .pretier.cache --ignore-unknown --write --insert-pragma .
# make a tarball
gtar -vcf ../Relational_Analysis_Vault.tar --exclude-tag-all=.tar_exclude.tag .
