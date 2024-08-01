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


SELECT COUNT(*) FROM STUDIES;
SELECT SUM(STUDIES.ID) FROM STUDIES;
SELECT AVG(STUDIES.ID) FROM STUDIES;
SELECT MIN(STUDIES.ID) FROM STUDIES;
SELECT MAX(STUDIES.ID) FROM STUDIES;


DO $$
DECLARE
    study_ids INT[];
    study_id INT;
    tag_id INT;
BEGIN
    -- Guardar os resultados do SELECT na variável study_ids
    SELECT ARRAY(SELECT s.id FROM studies AS s WHERE s.subject LIKE '%FastAPI%')
    INTO study_ids;

    -- Iterar sobre os study_ids e realizar operações para cada um
    FOREACH study_id IN ARRAY study_ids
    LOOP
        -- Inserir uma nova tag e obter o id
        INSERT INTO tags (tag_name)
        VALUES ('TesteTag')
        RETURNING id INTO tag_id;

        -- Criar o relacionamento na tabela study_tags
        INSERT INTO study_tags (study_id, tag_id)
        VALUES (study_id, tag_id);
    END LOOP;

    COMMIT;
END $$;



