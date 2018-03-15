# -*- coding: utf-8 -*-


# This is user information.
__NAME = ''
__AD = ''
__GRADE = ''
__SALE = ''

__MOVIES = ''


def get_user_grade():
    return __GRADE


def get_ad_agree():
    return __AD


def get_movie_seats(movie, index):
    return __MOVIES[movie].get_movie_seats()[index]


def set_info(*info):
    global __GRADE
    global __NAME
    global __AD
    global __SALE
    __GRADE = info[0]
    __NAME = info[1]
    __AD = info[2]
    __SALE = info[3]


def set_movies(movie):
    global __MOVIES
    __MOVIES = movie


def get_movies():
    return __MOVIES
