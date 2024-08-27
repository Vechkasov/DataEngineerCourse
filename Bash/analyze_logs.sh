#!/bin/bash

path_to_logs=access.log
path_to_report=report.txt

count_of_requests=$(cat $path_to_logs | awk '{ print $1 }' | wc -l)
count_of_unique_requests=$(cat $path_to_logs | awk '{ print $1 }' | sort | uniq | wc -l)

count_of_requests_group_by_methods=$(cat $path_to_logs | awk -F '"' '{print $2}' | awk '{print $1}' | sort | uniq -c)
most_popular_request=$(cat $path_to_logs | awk -F '"' '{print $2}' | awk '{print $2}' | sort | uniq -c | sort -rn | head -n 1)

if [ -f "$path_to_report" ]; then
	rm $path_to_report
fi

echo -e " Total count of requests: $count_of_requests\n" \
	"Total count of unique requests: $count_of_unique_requests\n\n" \
	"Total count of requests group by methods:\n$count_of_requests_group_by_methods\n\n" \
	"Most popular request URL: \n$most_popular_request" \
	>> $path_to_report

echo "Report saved in '$path_to_report'"