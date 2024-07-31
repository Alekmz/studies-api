-- Fazer uma busca que retorne os estudos junto a suas tags
SELECT 
    s.subject, 
    s.notes, 
    string_agg(t.tag_name, ', ') AS tag_names, -- Juntar as tags em uma coluna separa por virgulas para nao ter uma linha pra cada tag do mesmo estudo
    s.id 
FROM 
    studies AS s
JOIN 
    study_tags AS st ON s.id = st.study_id
JOIN 
    tags AS t ON st.tag_id = t.id
GROUP BY 
    s.id;


SELECT
	S.NOTES,
	S.SUBJECT,
	U.USERNAME,
	U.EMAIL
FROM
	STUDIES AS S
	JOIN USERS AS U ON U.ID = S.ID
WHERE
	U.ID = 1;