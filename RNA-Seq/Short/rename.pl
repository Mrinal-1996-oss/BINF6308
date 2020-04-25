#!/usr/bin/perl
use warnings;
use strict;
use feature qw(say);

my $infile="names.txt";
open(my $infh, "<", $infile);

my @arr;
my @real_names;

while(<$infh>){
	chomp $_;
	push @real_names, $_;
	$_=~s/\$//g;
	push @arr, $_;
}

for(my $i=0; $i<=25; $i++){
	`mv ./sam/$real_names[$i] $arr[$i]`; 
	}


