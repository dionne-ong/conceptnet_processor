from ..SqlConnector import SqlConnConcepts
from .Concept import Concept


class DBO_Concept:

    @staticmethod
    def getConcept(id):
        sql = "SELECT idconcepts, " \
              "relation," \
              "first," \
              "second " \
              "FROM concepts " \
              "WHERE idconcepts = %d;" % id

        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        resulting = None

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            result = cursor.fetchone()
            row = result
            id = row[0]
            relation = row[1]
            first = row[2]
            second = row[3]

            resulting = Concept(id, relation, first, second)

        except:
            print("Error Concepts: unable to fetch data of character #%d" % id)

        conn.close()
        return resulting

    @staticmethod
    def getAllConcepts():
        sql = "SELECT idconcepts, " \
              "relation," \
              "first," \
              "second " \
              "FROM concepts "

        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        resulting = []

        try:
            cursor.execute(sql)
            result = cursor.fetchall()

            for row in result:
                id = row[0]
                relation = row[1]
                first = row[2]
                second = row[3]

                resulting.append(Concept(id, relation, first, second))

        except:
            print("Error Concepts: unable to fetch all data")

        conn.close()
        return resulting

    @staticmethod
    def getConceptForWord(word):
        sql = "SELECT idconcepts, " \
              "relation," \
              "first," \
              "second " \
              "FROM concepts " \
              "WHERE first = %s OR second = %s "
        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        resulting = []

        try:
            cursor.execute(sql, (word, word,))
            # Fetch all the rows in a list of lists.
            result = cursor.fetchall()

            for row in result:
                id = row[0]
                relation = row[1]
                first = row[2]
                second = row[3]

            resulting.append(Concept(id, relation, first, second))

        except:
            print("Error Concept: unable to fetch data for word " + word)

        conn.close()
        return resulting

    @staticmethod
    def getConceptForWordRelation(word, relation):
        sql = "SELECT idconcepts, " \
              "relation," \
              "first," \
              "second " \
              "FROM concepts " \
              "WHERE (first = %s OR second = %s) AND relation = %s "
        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        resulting = []

        try:
            # Execute the SQL command
            cursor.execute(sql, (word, word, relation,))
            # Fetch all the rows in a list of lists.
            result = cursor.fetchall()

            for row in result:
                id = row[0]
                relation = row[1]
                first = row[2]
                second = row[3]

                resulting.append(Concept(id, relation, first, second))

        except:
            print("Error Concept: unable to fetch data for word " + word)

        conn.close()
        return resulting

    @staticmethod
    def addConcept(concept):
        sql = "INSERT INTO concepts " \
              "(relation, " \
              "first, " \
              "second) " \
              "VALUES " \
              "(%s, " \
              " %s, " \
              " %s);"
        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (concept.relation, concept.first, concept.second,))
            conn.commit()
            conn.close()
            return True

        except:
            print("Error Concept: unable to insert data " + concept.__str__())
            conn.close()
            return False

    @staticmethod
    def does_exist_relation(first, second, relation):
        sql = "SELECT * FROM concepts WHERE first = %s AND second = %s AND relation = %s"
        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (first, second, relation,))
            result = cursor.fetchall()
            ret = False

            if (len(result) > 0):
                ret = True

            conn.close()
            return ret

        except:
            print("Error Concept: unable to check data ", first,second)
            conn.close()
            return False

    @staticmethod
    def does_existn(word):
        sql = "SELECT * FROM concepts WHERE first = %s OR second = %s"
        conn = SqlConnConcepts.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (word, word,))
            result = cursor.fetchall()
            ret = False

            if (len(result) > 0):
                ret = True

            conn.close()
            return ret

        except:
            print("Error Concept: unable to check data " + word.__str__())
            conn.close()
            return False
