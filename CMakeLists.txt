cmake_minimum_required(VERSION 3.15)

project(CFD_ROOM_DESIGNER)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_subdirectory(src)