select errorfree projects:
	SELECT * FROM conversions WHERE CID NOT IN (SELECT CID FROM error_occurences);

select top 10 errors:
SELECT eo.EID,count(eo.EID) as errorcount, e.errortext from errors as e JOIN error_occurences as eo ON e.id = eo.EID GROUP BY eo.EID ORDER BY errorcount DESC LIMIT 10;

select CIDs with costume resulution warnings: 
SELECT eo.CID from errors as e JOIN error_occurences as eo ON e.id = eo.EID WHERE e.errortext like "%Costume resolution not same for all costumes%" GROUP BY eo.CID;
