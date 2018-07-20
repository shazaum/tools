#!/bin/bash

aws s3 mb s3://$2
aws s3 sync s3://$1 s3://$2
aws s3 rb --force s3://$1
