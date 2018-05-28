register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

filtered = FILTER ntriples BY (subject matches '.*rdfabout\\.com..*');
filtered2 = FOREACH filtered GENERATE subject as subject2, predicate as predicate2, object as object2;

joined = JOIN filtered BY object, filtered2 BY subject2;
joined = DISTINCT joined;

joined_group = GROUP joined ALL;
joined_count = FOREACH joined_group GENERATE COUNT(joined);

store joined_count into '/user/hadoop/q3b-result' using PigStorage();
