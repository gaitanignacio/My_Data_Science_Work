register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

filtered = FILTER ntriples BY (subject matches '.*business.*');
filtered2 = FILTER ntriples BY (subject matches '.*business.*');

joined = JOIN filtered BY subject, filtered2 BY subject;

joined_group = GROUP joined ALL;
joined_count = FOREACH joined_group GENERATE COUNT(joined);

store joined_count into '/home/hadoop/quiz/q3a-result' using PigStorage();
