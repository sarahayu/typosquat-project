# Notes

Improvement Points:
- pypi_unpopular.csv contains some popular packages, due to different casing, naming conventions, etc. 
- despite my hardest attempts, duplicates still occur e.g. zope-interface and zope.interface, because programmers can't keep consistent naming conventions

Some scripting tidbits


```sql
-- extract package name from filename rather than from project because project replaces periods with hyphens.
-- downside is that oftentimes this yields underscores in place of hyphens since filenaming convention uses underscores.
-- we will fix this during processing stage.

SELECT
  REGEXP_EXTRACT(
    file.filename,
    r'^(.+?)-' || REGEXP_REPLACE(file.version, r'[.+*?^${}()|[\]\\]', r'\\\0')
  ) AS package_name,
  COUNT(*) AS download_count
FROM
  `bigquery-public-data.pypi.file_downloads`
WHERE
  DATE(timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY
  package_name
HAVING
  download_count <= 15000
ORDER BY
  download_count DESC
```

```bash
# remove empty lines
for i in *.txt; do sed -i '/^\s*$/d' $i; done

# replace underscores with dashes, as extracting project names from filenames most often yields underscores in place of hyphens, as per file naming conventions
sed -i 's/\_/\-/g' pypi_popular.csv
sed -i 's/\_/\-/g' pypi_unpopular.csv
```