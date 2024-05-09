-- thid sql Lists all bands with Glam rock as their diffrent style, ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed)
AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
