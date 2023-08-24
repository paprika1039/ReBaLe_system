from gensim import models
import re

# Step1の処理を行うコサイン類似度計算の関数
def word2vec_step1(find_text,w2v_model):

    results = w2v_model.most_similar(positive=[find_text],topn=5)
    for result in results:
        print(result)

    return results[0], results[1], results[2]

# Step２からの処理を行うコサイン類似度の計算の関数
def word2vec_step2(find_text,w2v_model):

    results = w2v_model.most_similar(positive=[find_text],topn=10)
    for result in results:
        print(result)

    return results[0],results[1],results[2],results[3],results[4]

# Cypher作成用のコサイン類似度の結果をストックするための関数
def add_unique_items(word_stock, new_items):
    added = []
    for item in new_items:
        if item not in word_stock and item not in added:
            word_stock.append(item)
            added.append(item)
            if len(added) == 2: # 既に２つの新しい要素を追加したら処理を終了する
                break
    return word_stock

#複数の配列を１つにする関数
def concat_array(*args):
    result = []
    for item in args:
        if isinstance(item, list):
            result.extend(item)
        elif isinstance(item, str):
            result.append(item)
        else:
            result.append(item)

    return result




# input_key = input("enter your Idea\n")

def auto_word2vec(keyword, w2v_model):

    word_stock = []
    print("-----------------------------------")
    print("STEP1 search " + keyword)
    word_stock.append(keyword)
    layer1_1, layer1_2, layer1_3 = word2vec_step1(keyword, w2v_model)
    Llayer1_1 = list(layer1_1)
    Llayer1_2 = list(layer1_2)
    Llayer1_3 = list(layer1_3)
    print("selected word " + Llayer1_1[0] + ", " + Llayer1_2[0] + ", " + Llayer1_3[0])
    word_stock.append(Llayer1_1[0])
    word_stock.append(Llayer1_2[0])
    word_stock.append(Llayer1_3[0])
    print(word_stock)
    print("-----------------------------------\n")

    # STEP2-1
    print("-----------------------------------\n")
    print("STEP2-1 search " + Llayer1_1[0])
    layer2_11, layer2_12, layer2_13, layer2_14, layer2_15 = word2vec_step2(str(Llayer1_1[0]), w2v_model)
    Llayer2_11 = list(layer2_11)
    Llayer2_12 = list(layer2_12)
    Llayer2_13 = list(layer2_13)
    Llayer2_14 = list(layer2_14)
    Llayer2_15 = list(layer2_15)
    Llayer2_1 = concat_array(Llayer2_11[0], Llayer2_12[0], Llayer2_13[0], Llayer2_14[0], Llayer2_15[0])

    # STEP2-2
    print("-----------------------------------\n")
    print("STEP2-2 search " + Llayer1_2[0])
    layer2_21, layer2_22, layer2_23, layer2_24, layer2_25 = word2vec_step2(str(Llayer1_2[0]), w2v_model)
    Llayer2_21 = list(layer2_21)
    Llayer2_22 = list(layer2_22)
    Llayer2_23 = list(layer2_23)
    Llayer2_24 = list(layer2_24)
    Llayer2_25 = list(layer2_25)
    Llayer2_2 = concat_array(Llayer2_21[0], Llayer2_22[0], Llayer2_23[0], Llayer2_24[0], Llayer2_25[0])

    # STEP2-3
    print("-----------------------------------\n")
    print("STEP2-3 search " + Llayer1_3[0])
    layer2_31, layer2_32, layer2_33, layer2_34, layer2_35 = word2vec_step2(str(Llayer1_3[0]), w2v_model)
    Llayer2_31 = list(layer2_31)
    Llayer2_32 = list(layer2_32)
    Llayer2_33 = list(layer2_33)
    Llayer2_34 = list(layer2_34)
    Llayer2_35 = list(layer2_35)
    Llayer2_3 = concat_array(Llayer2_31[0], Llayer2_32[0], Llayer2_33[0], Llayer2_34[0], Llayer2_35[0])

    word_stock = add_unique_items(word_stock, Llayer2_1)
    word_stock = add_unique_items(word_stock, Llayer2_2)
    word_stock = add_unique_items(word_stock, Llayer2_3)

    print(word_stock)
    # print("selected word " + word_stock[4] + ", " + word_stock[5])
    # print("selected word " + word_stock[6] + ", " + word_stock[7])
    # print("selected word " + word_stock[8] + ", " + word_stock[9])
    print("-----------------------------------\n")

    return word_stock