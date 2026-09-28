#!/usr/bin/env python

import os
import uuid
import json
from datetime import time, date, datetime, timedelta
from random import randint
from random import choice

import click
import git

HELLO_WORLD_CPP = """#include <iostream>
int main()
{
  std::cout << "Hello World!" << std::endl;
  return 0;
}
"""

DEFAULT_FILE_NAME = 'main.cpp'

def subtract(art, hist):
    for r in range(len(art)):
        for c in range(len(art[r])):
            if 0 <= r < len(hist) and 0 <= c < len(hist[r]):
                art[r][c] = max(0, art[r][c] - hist[r][c])

class RockStar:

    def __init__(self, days=400, repo_path=False, days_off=(), file_name=DEFAULT_FILE_NAME,
                 code=HELLO_WORLD_CPP, off_fraction=0.0):
        self.days = days
        self.code = code
        if repo_path:
            self.repo_path = repo_path
        else:
            self.repo_path = os.getcwd()
        self.file_name = file_name
        self.file_path = os.path.join(self.repo_path, file_name)
        self.messages_file_name = 'commit-messages.json'
        self.messages_file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), self.messages_file_name)
        self.days_off = list(map(str.capitalize, days_off))
        self.off_fraction = off_fraction

        self._load_commit_messages()

    def _load_commit_messages(self):
        with open(self.messages_file_path) as f:
            messages_file_contents = json.load(f)
        names = messages_file_contents['names']
        messages = messages_file_contents['messages']
        self.commit_messages = [m.format(name=choice(names)) for m in messages]

    def _get_random_commit_message(self):
        return choice(self.commit_messages)

    def _make_last_commit(self):
        with open(self.file_path, 'w') as f:
            f.write(self.code)

        os.environ['GIT_AUTHOR_DATE'] = ''
        os.environ['GIT_COMMITTER_DATE'] = ''
        self.repo.index.add([self.file_path])
        self.repo.index.commit('Final commit :sunglasses:')

    def _edit_and_commit(self, message, commit_date):
        with open(self.file_path, 'w') as f:
            f.write(message)
        self.repo.index.add([self.file_path])
        date_in_iso = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        os.environ['GIT_AUTHOR_DATE'] = date_in_iso
        os.environ['GIT_COMMITTER_DATE'] = date_in_iso
        self.repo.index.commit(self._get_random_commit_message())

    @staticmethod
    def _get_random_time():
        return time(hour=randint(0, 23), minute=randint(0, 59),
                    second=randint(0, 59), microsecond=randint(0, 999999))

    def _get_dates_list(self):

#         def dates():
#             today = date.today()
#             for day_delta in range(self.days):
#                 day = today - timedelta(days=day_delta)
#                 if day.strftime('%A') in self.days_off:
#                     continue
#                 if randint(1, 100) < self.off_fraction * 100:
#                     continue
#                 for i in range(randint(1, 10)):
#                     yield day
        R = 10
        H = 6
        M = 3
        L = 1


        winamp = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, L, 0, L, 0, 0, 0, L, 0, 0, 0],
            [0, 0, L, 0, L, 0, 0, 0, L, 0, 0, 0, L, 0, 0, 0, L, 0, L, 0, 0, 0, L, 0, L, 0],
            [0, 0, M, 0, M, 0, 0, 0, M, 0, M, 0, M, 0, 0, 0, M, 0, M, 0, 0, 0, M, 0, M, 0],
            [M, 0, M, 0, M, 0, M, 0, M, 0, M, 0, M, 0, 0, 0, M, 0, M, 0, M, 0, M, 0, M, 0],
            [R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0],
            [R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0, R, 0],
        ]
        pacman = [
            [0, M, M, M, 0, 0, 0, 0, R, R, R, 0, 0, 0, 0, 0, L, L, L, 0, 0, 0, 0, 0, 0, 0],
            [M, M, M, M, M, 0, 0, R, R, R, R, R, 0, 0, 0, L, L, L, L, L, 0, 0, 0, 0, 0, 0],
            [M, 0, M, 0, M, 0, 0, R, 0, R, 0, R, 0, 0, L, L, L, L, 0, 0, 0, L, 0, 0, 0, 0],
            [M, H, M, H, M, 0, 0, R, H, R, H, R, 0, 0, L, L, L, 0, 0, 0, L, L, L, 0, 0, L],
            [M, M, M, M, M, 0, 0, R, R, R, R, R, 0, 0, L, L, L, L, 0, 0, 0, L, 0, 0, 0, 0],
            [M, M, M, M, M, 0, 0, R, R, R, R, R, 0, 0, 0, L, L, L, L, L, 0, 0, 0, 0, 0, 0],
            [M, 0, M, 0, M, 0, 0, R, 0, R, 0, R, 0, 0, 0, 0, L, L, L, 0, 0, 0, 0, 0, 0, 0],
        ]
        hist = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        art = winamp
        subtract(art, hist)

        # Start on the Sunday 31 weeks ago
        # (Seems like GitHub isn't populating the graph before that)
        start = date.today()
        if start.weekday() < 6:
            start = start - timedelta(days=start.weekday()+1)
        start = start - timedelta(days=31*7)
        date_string = '2022-08-28'
        start = datetime.strptime(date_string, '%Y-%m-%d')

        # print(start)
        # exit

        total_days = len(art) * len(art[0])

        dates = []

        for day_delta in range(total_days):
            day = start + timedelta(days=day_delta)

            commit_count = art[day_delta % 7][day_delta // 7]

            for commit_number in range(commit_count):
                dates.append(day)

        return [datetime.combine(d, self._get_random_time())
                for d in dates]




    def make_me_a_rockstar(self):
        self.repo = git.Repo.init(self.repo_path)
        label = 'Making you a Rockstar Programmer'
        # arr = self._get_dates_list()
        # print(arr[0])
        # return

        with click.progressbar(self._get_dates_list(), label=label) as bar:
            for commit_date in bar:
                self._edit_and_commit(str(uuid.uuid1()), commit_date)
        self._make_last_commit()
        print('\nYou are now a Rockstar Programmer!')


@click.command()
@click.option('--days', type=int, default=400)
@click.option('--repo_path')
def cli(days):
    magic = RockStar(days=days, repo_path=repo_path)
    magic.make_me_a_rockstar()
