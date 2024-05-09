-- data banse thatscript that ranks country origins of bands,
-- in ordered to by the number of (non-unique) fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
