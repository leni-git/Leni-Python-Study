# -*- coding:utf-8 -*-

# 프로그램 동작에 대한 메뉴를 사용자가 알 수 있도록 출력
def menu(grade):

    if grade=="0":
        print """\n- - - - - - - - - - - - - - - - - -
        1. 영화 예매
        2. 영화 상영시간 확인
        3. 영화 관리
        4. 총 수입확인
        5. 프로그램 종료
- - - - - - - - - - - - - - - - - -"""

    elif grade=="1":
        print """\n- - - - - - - - - - - - - - - - - -
        1. 영화 예매
        2. 영화 상영시간 확인
        3. 프로그램 종료
- - - - - - - - - - - - - - - - - -"""
    
    return "menu()"

# Employee 등급인 경우 보이는 영화 관리 메뉴를 사용자가 알 수 있도록 출력
def management_menu() :

    print """\n- - - - - - - - - - - - - - - - - -
     1. 상영영화 추가
     2. 상영영화 수정
     3. 상영영화 삭제
     4. 메인으로 돌아가기
- - - - - - - - - - - - - - - - - -"""

    return "management_menu()"

#사용자가 선택한 영화에 좌석의 예약 정보를 사용자가 알 수 있도록 출력
def print_seat(seat):
    print "\n____________S C R E E N____________\n"
    print "\t   ",
    for i in range(1, 6) : print "  "+str(i)+" ",
    print ""
    for i in range(ord('A'), ord('F')):
        print "\t",
        print chr(i), " ",
        for j in range(1, 6):
            if seat.get((chr(i), j))==0: print" ○ ",
            elif seat.get((chr(i), j))==1: print" ● ",
        print ""
    print "\n________좌석 예약 상황입니다________"


# 영화목록에 대한 정보 출력
def print_movie(command, movies) :

    print "\n- - - - 영화를 선택해주세요 - - - - \n"
    for i in range(len(movies)) :
        print str(i+1), ". ", movies[i].get_movie_name()
        print " ", movies[i].get_movie_times()
        print "\n",
    # 영화제목, 상영시간 순으로 입력받기. ( 정규형식 부분 참조하기 )
    #for i in range(0, len(movieList)): print "        " + str(i + 1) + ". " + movieList[i].mName
    print "- - - - - - - - - - - - - - - - - - "
    return command

