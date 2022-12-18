-- create our database and tables
CREATE TABLE task (
    id INTEGER PRIMARY KEY,
    summary VARCHAR(1024),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

-- POPULATE OR TABLE WHIT SOME DATA

INSERT INTO task (
    summary,
    description
) VALUES (
    "Take out the trash",
    "Take the trash out to th dumpster by the driveway" 
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Do the dishes",
    "Wash the dishes in the sink" 
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Mow the lawn",
    "Mow the lawn in the backyard" 
);

