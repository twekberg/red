#!/usr/bin/env python
"""
Manage a database
"""


import argparse
import sqlite3
import sys


class Db():
    """
    Manage a database.
    """
    def __init__(self, db_file=None):
        """Initializes the data structures."""
        self.con = sqlite3.connect(db_file)

    def get_cursor(self):
        """
        Get DB cursor.
        """
        return self.con.cursor()

    def execute(self, sql, values=None):
        """
        Execute a query and return the resulots.
        Pass values if there are :things in the query (or INSERT).
        """
        cur = self.get_cursor()
        cur.execute(sql, values if values else {})
        return cur.fetchall()

    def close(self):
        """
        Close the database
        """
        self.con.close()
