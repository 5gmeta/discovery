#!/bin/bash


discovery_url="http://127.0.0.1:8282"
answer_path="/tmp"
reference_path="reference"
fecha=`date +%Y%m%d-%H%M%S`
log_file="tests"$fecha".log"
echo "test,result" > $log_file


check_and_write_log () {
    local test_name=$1 
    answer_file=$answer_path"/"$test_name"_answer.json"
    reference_file=$reference_path"/"$test_name"_answer.json"
    diff <(jq --sort-keys . $answer_file) <(jq --sort-keys . $reference_file) 
    if [[ $? == 0 ]]
        then
            echo "$test_name,YES" >> $log_file 
        else
            echo "$test_name,NO" >> $log_file
    fi
}

## Get no MEC

test_name="get_no_mec"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"


curl -X GET $discovery_url"/mec" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name 


## Add a MEC

test_name="new_mec"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"

curl -X POST $discovery_url"/mec" -H 'accept: */*'  -H "Content-Type: application/json" -d @register_mec_example.json > $answer_file
check_and_write_log $test_name 


## Get MEC

test_name="get_mec"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"


curl -X GET $discovery_url"/mec" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name 

## Get MEC locations

test_name="get_mec_locations"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"

curl -X GET $discovery_url"/mec/locations" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name 


## Get list tiles

test_name="get_list_tiles"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"

curl -X GET $discovery_url"/mec/tile" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name



## Get MEC from tile

test_name="get_mec_from_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile="031333123201212"


curl -X GET $discovery_url"/mec/tile/$tile" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name


## Get MEC from tile that is composed of multiple MEC

test_name="get_multiple_mec_from_bigger_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile="0313331232"


curl -X GET $discovery_url"/mec/tile/$tile" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name


## Get MEC from tile wrong

test_name="get_mec_from_tile_wrong"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile="000000"


curl -X GET $discovery_url"/mec/tile/$tile" -H 'accept: */*'  -H "Content-Type: application/json"  > $answer_file

check_and_write_log $test_name


## Add tile

test_name="add_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_added="10000000"
mec="1"
curl -X 'POST' $discovery_url"/mec/$mec/tile/"$tile_to_be_added -H 'accept: */*' > $answer_file
check_and_write_log $test_name


## Add existing tile

test_name="add_existing_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_added="10000000"
mec="1"
curl -X 'POST' $discovery_url"/mec/$mec/tile/"$tile_to_be_added -H 'accept: */*' > $answer_file
check_and_write_log $test_name 

## Add containing tile

test_name="add_containing_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_added="1000000"
mec="1"
curl -X 'POST' $discovery_url"/mec/$mec/tile/"$tile_to_be_added -H 'accept: */*' > $answer_file
check_and_write_log $test_name 


## Add contained tile

test_name="add_contained_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_added="1000000000"
mec="1"
curl -X 'POST' $discovery_url"/mec/$mec/tile/"$tile_to_be_added -H 'accept: */*' > $answer_file
check_and_write_log $test_name



## delete tile

test_name="delete_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_deleted="1000000"
mec="1"
curl -X 'DELETE' $discovery_url"/mec/$mec/tile/"$tile_to_be_deleted -H 'accept: */*' > $answer_file
check_and_write_log $test_name

## delete non existing tile

test_name="delete_non_existing_tile"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
tile_to_be_deleted="200000"
mec="1"
curl -X 'DELETE' $discovery_url"/mec/$mec/tile/"$tile_to_be_deleted -H 'accept: */*' > $answer_file
check_and_write_log $test_name 

exit

## Delete MEC
test_name="delete_mec"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
mec_to_be_deleted="1"
curl -X 'DELETE' $discovery_url"/mec/"$mec_to_be_deleted -H 'accept: */*' > $answer_file

check_and_write_log $test_name 



## Delete MEC doesn't exists
test_name="delete_mec_no_exists"
answer_file=$answer_path"/"$test_name"_answer.json"
reference_file=$reference_path"/"$test_name"_answer.json"
mec_to_be_deleted="10"
curl -X 'DELETE' $discovery_url"/mec/"$mec_to_be_deleted -H 'accept: */*' > $answer_file

check_and_write_log $test_name 


