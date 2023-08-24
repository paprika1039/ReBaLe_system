from py2neo import Graph, Node, Relationship
import os
import re
from bardapi import Bard
import webbrowser
from neo4j import GraphDatabase


os.environ['_BARD_API_KEY']="ZgjrUPCdzXh4OG5htuAAoAvKNCXr5p7Q8OP1ml04BabmjWOSS2JzD4G2w7SGCWjlG2yAPA."
graph = Graph("bolt://localhost:7687", auth=("neo4j", "fumiaki1039"))

# username = "fumi"

def google_search_link(query):
    search_url = f"https://www.google.com/search?q={query}"
    return f'<a href="{search_url}" target="_blank">{query}</a>'

def remove_symbols(text):
    # 正規表現を使用して文字列中の記号を削除する
    return re.sub(r'[^\w\sー]', '', text)

def create_tree(word_stock, username, challenge):
    tx = graph.begin()

    nodes = []

    for i, word in enumerate(word_stock):
        if i == 0:
            print(type(word))
            node = Node("step0", username, name=word, url=google_search_link(word))
            nodes.append(node)
            tx.create(node)
        elif i < 4:
            node = Node("step1", username, name=word, url=google_search_link(word))
            nodes.append(node)
            tx.create(node)
            # relation = Relationship(nodes[0], "Relation_type", node)
            # tx.create(relation)
            if i ==1:
                print("area 1")
                relation = Relationship(nodes[0], "Relation_type", node, name="relation")
                tx.create(relation)
            if i ==2:
                print("area 2")
                relation = Relationship(nodes[0], "Relation_type", node, name="relation")
                tx.create(relation)
            if i ==3:
                print("area 3")
                relation = Relationship(nodes[0], "Relation_type", node, name="relation")
                tx.create(relation)
            
        else:
            print(i)
            node = Node("step2", username, name=word, url=google_search_link(word))
            nodes.append(node)
            tx.create(node)
            if i ==4 or i ==5:
                print("area 4~5")
                relation = Relationship(nodes[1], "Relation_type", node, name="relation")
                tx.create(relation)
            if i ==6 or i ==7:
                print("area 6~7")
                relation = Relationship(nodes[2], "Relation_type", node, name="relation")
                tx.create(relation)
            if i ==8 or i ==9:
                print("area 8~9")
                relation = Relationship(nodes[3], "Relation_type", node, name="relation")
                tx.create(relation)
        # if i > 0:
        #     relation = Relationship(nodes[0], "Relation_type", node)
        #     tx.create(relation)
    print("before use bard")
    sample_data = Bard().get_answer(challenge + "を使用したサービスを説明文なしの単語で羅列してください")['content']

    # 各行をリストに分割
    lines = [line.strip() for line in sample_data.split('\n') if line.strip() != '']

    # 各行の先頭と末尾の空白文字を除去し、記号を省いた後で15文字以下の文字列を抽出してリストに格納
    result = [remove_symbols(line.strip()) for line in lines if len(remove_symbols(line.strip())) <= 10]

    # 結果を出力
    for item in result:
        print(type(item))
        print(item)
    # graph = Graph("bolt://localhost:7687", auth=("neo4j", "fumiaki1039"))
    # parent_node = Node("step1", name=enter_key)
    # graph.create(parent_node)

    # curent_parent_node = parent_node

    for i in range(0, len(result)):
        node = Node("step4", username, name=str(result[i]), url=google_search_link(str(result[i])))
        tx.create(node)
        relation = Relationship(nodes[0], "things", node, name="things")
        tx.create(relation)

    tx.commit()
