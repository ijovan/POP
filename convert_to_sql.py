from source.csv_file import CSVFile
import datetime
import re
import os


INPUT_DIR = "output"
OUTPUT_DIR = "sql"

if not os.path.isdir(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class Table:
    IN_NAME = None
    TABLE_NAME = None
    HEADER = []

    def __init__(self):
        self.items = []
        self.sql_rows = []
        self.input_file = CSVFile(self.input_path())

    def input_path(self):
        return '/'.join([INPUT_DIR, self.IN_NAME]) + '.csv'

    def output_path(self):
        return '/'.join([OUTPUT_DIR, self.TABLE_NAME]) + '.sql'

    def read(self):
        rows = self.input_file.read()
        header = rows.pop(0)

        for row in rows:
            self.items.append(dict(zip(header, row)))

    def write(self):
        if not self.sql_rows:
            self.generate_sql_rows()

        output_file = open(self.output_path(), "w")

        for row in self.sql_rows:
            output_file.write(row)

        output_file.close()

    def generate_sql_rows(self):
        if not self.items:
            self.read()

        self.sql_rows = []

        for row in self.items:
            self.sql_rows.append(f"INSERT INTO {self.TABLE_NAME} "
                + f"({', '.join(self.HEADER)}) "
                + f"VALUES ({', '.join(self.map_row(row))});\n")

    def map_row(self, row):
        return list(row.values())

NULL = "NULL"

class Field:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def to_s(self):
        if self.raw_value:
            return self.raw_value
        else:
            return NULL

class Id:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def to_s(self):
        if self.raw_value == "-1":
            return NULL
        elif self.raw_value:
            return self.raw_value
        else:
            return NULL

class Boolean(Field):
    def to_s(self):
        if self.raw_value == "True":
            return "1"
        elif self.raw_value == "False":
            return "0"
        else:
            return NULL

class String(Field):
    def to_s(self):
        if self.raw_value:
            string = re.sub(r'([^\x20-\x7E]|&)+', '', self.raw_value)

            return f"'{string}'"
        else:
            return NULL

class Date(Field):
    def to_s(self):
        if self.raw_value:
            timestamp = \
                datetime.datetime.fromtimestamp(int(self.raw_value))

            time_string = timestamp.strftime("%d-%m-%Y")

            return f"'{time_string}'"
        else:
            return NULL

class Answer(Table):
    IN_NAME = "answers"
    TABLE_NAME = "Answer"
    HEADER = [
        "ans_id", "ans_qst_id", "ans_usr_id", "ans_last_edit_date",
        "ans_last_activity_date","ans_score", "ans_is_accepted",
        "ans_creation_date"
    ]

    def map_row(self, row):
        fields = [
            Id(row['id']),
            Id(row['question_id']),
            Id(row['owner_id']),
            Date(row['last_edit_date']),
            Date(row['last_activity_date']),
            Field(row['score']),
            Boolean(row['is_accepted']),
            Date(row['creation_date'])
        ]

        return [field.to_s() for field in fields]

class Comment(Table):
    IN_NAME = "comments"
    TABLE_NAME = "Comment_OLTP"
    HEADER = [
        "cmt_id", "cmt_to_usr_id", "cmt_pst_usr_id", "cmt_edited",
        "cmt_post_type", "cmt_post_id", "cmt_link", "cmt_score",
        "cmt_creation_date", "cmt_ans_id", "cmt_qst_id"
    ]

    def map_row(self, row):
        fields = [
            Id(row['id']),
            Id(row['reply_to_user_id']),
            Id(row['owner_id']),
            Boolean(row['edited']),
            String(row['post_type']),
            Id(row['post_id']),
            String(row['link']),
            Field(row['score']),
            Date(row['creation_date'])
        ]

        if row['post_type'] == 'question':
            fields.append(Field(None))
            fields.append(Id(row['post_id']))
        elif row['post_type'] == 'answer':
            fields.append(Id(row['post_id']))
            fields.append(Field(None))

        return [field.to_s() for field in fields]

class Question(Table):
    IN_NAME = "questions"
    TABLE_NAME = "Question"
    HEADER = [
        "qst_id", "qst_pst_usr_id", "qst_bnt_usr_id", "qst_edt_usr_id",
        "qst_acpt_ans_id", "qst_bounty_amount", "qst_bounty_closes_date",
        "qst_closed_date", "qst_closed_reason", "qst_locked_date",
        "qst_favourite_count", "qst_creation_date", "qst_view_count",
        "qst_up_vote_count", "qst_last_activity_date", "qst_last_edit_date",
        "qst_link", "qst_score"
    ]

    def map_row(self, row):
        fields = [
            Id(row['id']),
            Id(row['owner_id']),
            Id(row['bounty_user_id']),
            Id(row['last_editor_id']),
            Id(row['accepted_answer_id']),
            Field(row['bounty_amount']),
            Date(row['bounty_closes_date']),
            Date(row['closed_date']),
            String(row['closed_reason']),
            Date(row['locked_date']),
            Field(row['favorite_count']),
            Date(row['creation_date']),
            Field(row['view_count']),
            Field(row['up_vote_count']),
            Date(row['last_activity_date']),
            Date(row['last_edit_date']),
            String(row['link']),
            Field(row['score'])
        ]

        return [field.to_s() for field in fields]

class Tag(Table):
    IN_NAME = "tags"
    TABLE_NAME = "Tag"
    HEADER = ["tag_name", "tag_cat_id", "tag_last_activity_date"]

    def map_row(self, row):
        fields = [
            String(row['name']),
            Field(None),
            Date(row['last_activity_date'])
        ]

        return [field.to_s() for field in fields]

class TagQuestion(Table):
    IN_NAME = "tags_questions"
    TABLE_NAME = "Tagged_Question"
    HEADER = ["qst_id", "tag_name"]

    def map_row(self, row):
        fields = [
            Id(row['question_id']),
            String(row['tag_id'])
        ]

        return [field.to_s() for field in fields]

class TagSynonym(Table):
    IN_NAME = "tag_synonyms"
    TABLE_NAME = "TagSynonym"
    HEADER = [
        "syn_to_tag_name", "syn_from_tag_name", "syn_last_applied_date",
        "syn_creation_date"
    ]

    def map_row(self, row):
        fields = [
            String(row['to_tag']),
            String(row['from_tag']),
            Date(row['last_applied_date']),
            Date(row['creation_date'])
        ]

        return [field.to_s() for field in fields]

class User(Table):
    IN_NAME = "users"
    TABLE_NAME = "User_OLTP"
    HEADER = [
        "usr_id", "usr_account_id", "usr_age", "usr_creation_date",
        "usr_display_name", "usr_is_employee", "usr_last_access_date",
        "usr_last_modified_date", "usr_location", "usr_reputation",
        "usr_type", "usr_up_vote_count", "usr_down_vote_count",
        "usr_view_count"
    ]

    def map_row(self, row):
        fields = [
            Id(row['id']),
            Id(row['account_id']),
            Field(row['age']),
            Date(row['creation_date']),
            String(row['display_name']),
            Boolean(row['is_employee']),
            Date(row['last_access_date']),
            Field(None),
            String(row['location']),
            Field(row['reputation']),
            String(row['type']),
            Field(row['up_vote_count']),
            Field(row['down_vote_count']),
            Field(row['view_count'])
        ]

        return [field.to_s() for field in fields]

Answer().write()
Comment().write()
Question().write()
Tag().write()
TagQuestion().write()
TagSynonym().write()
User().write()
