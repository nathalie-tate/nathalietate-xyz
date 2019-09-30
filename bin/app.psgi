#!/usr/bin/env perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/../lib"; 

use nathalietate::xyz; 
#use nathalietate::xyz_admin;

use Plack::Builder;

builder {
    mount '/'      => nathalietate::xyz->to_app;
    #mount '/admin'      => nathalietate::xyz_admin->to_app;
}
