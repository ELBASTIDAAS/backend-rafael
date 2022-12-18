-- create our database and tables

CREATE TABLE task (
    id INTEGER PRIMARY KEY,
    sumary VARCHAR(1024)
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
);

-- pOPULATE OR TABLE WHIT SOME DATA

INSERT INTO TABLE task (
    summary,
    description,
    is_active
) VALUES (
    "Take out the trash",
    "Take the trash out to th dumpster by the driveway" 
);

INSERT INTO TABLE task (
    summary,
    description,
    is_active
) VALUES (
    "Do the dishes",
    "Wash the dishes in the sink" 
);

INSERT INTO TABLE task (
    summary,
    description,
    is_active
) VALUES (
    "Mow the lawn",
    "Mow the lawn in the backyard" 
);

