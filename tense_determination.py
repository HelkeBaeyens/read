# English tenses will be determined

from nltk import word_tokenize, pos_tag
import unittest
import re

def determine_tense_input(sentence):
    tense = []

    text = word_tokenize(sentence.lower())
    tagged_tup = pos_tag(text)
    #print (tagged_tup)
    tags = [tuple[1] for tuple in tagged_tup]
    words = [tuple[0] for tuple in tagged_tup]
    tags_strings = " ".join(tags)
    words_strings = " ".join(words)
    tags_words_strings = " ".join([tuple[0]+ "_" + tuple[1] for tuple in tagged_tup])
    #print (words_strings)
    #print (tags_strings)
    #print (tags_words_strings)

    dict_tenses1 = {\
        r"(PRP.*VBD)" : "past_simple_affirmative",
        r"(PRP.*VBP)|(VBZ.*\._\.)" : "present_simple_affirmative"
        }
    dict_tenses2 = {\
        r"(do not)|(does not)|(am not)|(is not)|(cannot)|(can not)|(do n't)|(ca n't)|(am n't)" : "present_simple_negative",
        r"(did not)|(did n't)|(didn't)" : "past_simple_negative",
        r"(has been)|(have been)" : "present_perfect_affirmative",
        r"(has not been)|(has n't been)|(hasn't been)|(have not been)|(haven't been)|(have n't been)" : "present_perfect_negative",
        }

    dict_tenses3 = {\
        r"(do.*PRP.*VB.*\?)|(does.*PRP.*VB.*\?)|(do.*PRP.*VBP.*\?)|(does.*PRP.*VBP.*\?)" : "present_simple_interrogative",
        r"(did.*PRP.*VB.*\?)|(did.*PRP.*VBP.*\?)" : "past_simple_interrogative",
        r"(is.*VBG.*\._\.)|(am.*VBG.*\._\.)|(are.*VBG.*\._\.)" : "present_continuous_affirmative",
        r"(was.*VBG.*\._\.)|(were.*VBG.*\._\.)" : "past_continuous_affirmative",
        r"(is.*n't.*VBG.*\._\.)|(is.*not.*VBG.*\._\.)|(are.*n't.*VBG.*\._\.)|(are.*not.*VBG.*\._\.)|('m.*not.*VBG.*\._\.)|(am.*not.*VBG.*\._\.)" : "present_continuous_negative",
        r"(was.*n't.*VBG.*\._\.)|(was.*not.*VBG.*\._\.)|(wasn't.*VBG.*\._\.)|(were.*n't.*VBG*.\._\.)|(were.*not.*VBG.*\._\.)|(weren't.*VBG.*\._\.)" : "past_continuous_negative",
        r"(is.*PRP.*VBG.*\?)|(am.*PRP.*VBG.*\?)|(are.*PRP.*VBG.*\?)" : "present_continuous_interrogative",
        r"(was.*PRP.*VBG.*\?)|(were.*PRP.*VBG.*\?)" : "past_continuous_interrogative",
        r"(have.*PRP.*been.*\?)|(has.*PRP.*been.*\?)" : "present_perfect_interrogative",
        r"(have.*been.*VBG.*\._\.)|(has.*been.*VBG.*\._\.)|('ve.*been.*VBG.*\._\.)" : "present_perfect_continuous_affirmative",
        r"(have.*not.*been.*VBG.*\._\.)|(haven't.*been.*VBG.*\._\.)|(have.*n't.*been.*VBG.*\._\.)|(has.*not.*been.*VBG.*\._\.)|(hasn't.*been.*VBG.*\._\.)|(has.*n't.*been.*VBG.*\._\.)" : "present_perfect_continuous_negative",
        r"(have.*PRP.*been.*VBG.*\?)|(has.*PRP.*been.*VBG.*\?)" : "present_perfect_continuous_interrogative",
        r"(had.*VBN.*\._\.)" : "past_perfect_affirmative",
        r"(had.*not.*VBN.*\._\.)|(hadn't.*VBN.*\._\.)|(had.*n't.*VBN.*\._\.)" : "past_perfect_negative",
        r"(had.*PRP.*VBN.*\?)" : "past_perfect_interrogative",
        r"(had.*been.*VBG.*\._\.)" : "past_perfect_continuous_affirmative",
        r"(had.*not.*been.*VBG.*\._\.)|(had.*n't.*been.*VBG.*\._\.)|(hadn't.*been.*VBG.*\._\.)" : "past_perfect_continuous_negative",
        r"(had.*PRP.*been.*VBG.*\?)" : "past_perfect_continuous_interrogative",
        r"(will.*VB.*\._\.)" : "future_simple_affirmative",
        r"(wo.*n't.*VB.*\._\.)|(will.*not.*VB.*\._\.)|(will.*n't.*\._\.)" : "future_simple_negative",
        r"(will.*PRP.*VB.*\?)" : "future_simple_interrogative",
        r"(will.*be.*VBG.*\._\.)" : "future_continuous_affirmative",
        r"(won't.*be.*VBG.*\._\.)| (will.*not.*VBG.*\._\.)|(will.*n't.*VBG.*\._\.)" :"future_continuous_negative",
        r"(will.*PRP.*be.*VBG.*\?)" : "future_continuous_interrogative",
        r"(will.*have.*VBN.*\._\.)" : "future_perfect_affirmative",
        r"(won't.*have.*VBN.*\._\.)|(will.*not.*have.*VBN.*\._\.)|(will.*n't have.*VBN.*\._\.)" : "future_perfect_affirmative",
        r"(will.*PRP.*have.*VBN.*\?)" : "future_perfect_interrogative",
        r"(will.*have.*been.*VBG.*\._\.)" : "future_perfect_continuous_affirmative",
        r"(won't.*have.*been.*VBG.*\._\.)|(will.*not.*have.*been.*VBG.*\._\.)|(will.*n't.*have.*been.*VBG.*\._\.)" : "future_perfect_continuous_negative",
        r"(will.*PRP.*have.*been.*VBG.*\?)" : "future_perfect_continuous_interrogative",
        r"(would.*VB.*\._\.)" : "conditional_affirmative",
        r"(wouldn't_VB.*\._\.)|(would.*not_VB.*\._\.)|(would.*n't_VB.*\._\.)" : "conditional_negative",
        r"(would.*PRP.*VB.*\?)" : "conditional_interrogative",
        r"(would.*be.*VBG.*\._\.)" :"conditional_continuous_affirmative",
        r"(wouldn't.*be.*VBG.*\._\.)|(would.*not.*VBG.*\._\.)|(would.*n't.*VBG.*\._\.)" : "conditional_continuous_negative",
        r"(would.*PRP.*be.*VBG.*\?)" : "conditional_continuous_interrogative",
        r"(would.*have.*VBN.*\._\.)" : "conditional_perfect_affirmative",
        r"(wouldn't.*have.*VNB.*\._\.)|(would.*not.*have.*VBN.*\._\.)|(would.*n't.*have.*VBN.*\._\.)" : "conditional_perfect_negative",
        r"(would.*PRP.*have.*VBG.*\?)" : "conditional_perfect_interrogative",
        r"(is.*going.*TO.*VBN.*\._\.)|('s.*going.*TO.*VBN.*\._\.)|(am.*going.*TO.*VBN.*\._\.)|(are.*going.*TO.*VBN.*\._\.)|('re.*going.*TO.*VBN.*\._\.)|('m.*going.*TO.*VBN.*\._\.)" : "future_going_to_affirmative",
        r"(is.*n't.*going.*TO.*VBN.*\._\.)|(is.*not.*going.*TO.*VBN.*\._\.)|(are.*n't.*going.*TO.*VBN.*\._\.)|(are.*not.*going.*TO.*VBN.*\._\.)|('m.*not.*going.*TO.*VBN.*\._\.)|(am.*not.*going.*TO.*VBN.*\._\.)" : "future_going_to_negative",
        r"(is.*PRP.*going.*TO.*VBN.*\?)|(am.*PRP.*going.*TO.*VBN.*\?)|('s.*PRP.*going.*TO.*VBN.*\?)|('m.*PRP.*going.*TO.*VBN.*\?)|(are.*PRP.*going.*TO.*VBN.*\?)|('re.*PRP.*going.*TO.*VBN.*\?)" : "future_going_to_interrogative"
        }
    for tense_regex in dict_tenses3:
        if re.search (tense_regex, tags_words_strings):
            tense.append (dict_tenses3[tense_regex])

    if len (tense)==0:
        for tense_regex in dict_tenses2:
            if re.search (tense_regex, words_strings):
                tense.append (dict_tenses2[tense_regex])

    if len (tense)==0:
        for tense_regex in dict_tenses1:
            if re.search (tense_regex, tags_strings):
                tense.append (dict_tenses1[tense_regex])
    return(tense)

def level_of_tenses (tense):
    dict_level = {
        "past_simple_affirmative":"A1",
        "present_simple_affirmative":"A1",
        "present_simple_negative":"A1",
        "past_simple_negative":"A1",
        "present_perfect_affirmative":"A2",
        "present_perfect_negative":"A2",
        "present_simple_interrogative":"A1",
        "past_simple_interrogative":"A1",
        "present_continuous_affirmative":"A1",
        "past_continuous_affirmative":"A2",
        "present_continuous_negative":"A1",
        "past_continuous_negative":"A2",
        "present_continuous_interrogative":"A1",
        "past_continuous_interrogative":"A2",
        "present_perfect_interrogative":"A2",
        "present_perfect_continuous_affirmative":"B2",
        "present_perfect_continuous_negative":"B2",
        "present_perfect_continuous_interrogative":"B2",
        "past_perfect_affirmative":"B1",
        "past_perfect_negative":"B1",
        "past_perfect_interrogative":"B1",
        "past_perfect_continuous_affirmative":"B2",
        "past_perfect_continuous_negative":"B2",
        "past_perfect_continuous_interrogative":"B2",
        "future_simple_affirmative":"A2",
        "future_simple_negative":"A2",
        "future_simple_interrogative":"A2",
        "future_continuous_affirmative":"A2",
        "future_continuous_negative":"A2",
        "future_continuous_interrogative":"A2",
        "future_perfect_affirmative":"B2",
        "future_perfect_affirmative":"B2",
        "future_perfect_interrogative":"B2",
        "future_perfect_continuous_affirmative":"B2",
        "future_perfect_continuous_negative":"B2",
        "future_perfect_continuous_interrogative":"B2",
        "conditional_affirmative":"A1",
        "conditional_negative":"A1",
        "conditional_interrogative":"A1",
        "conditional_continuous_affirmative":"C1",
        "conditional_continuous_negative":"C1",
        "conditional_continuous_interrogative":"C1",
        "conditional_perfect_affirmative":"C1",
        "conditional_perfect_negative":"C1",
        "conditional_perfect_interrogative":"C1",
        "future_going_to_affirmative":"A2",
        "future_going_to_negative":"A2",
        "future_going_to_interrogative":"A2",
    }
    return dict_level.get(tense)

class My_test(unittest.TestCase):

    def test_psa(self):
        self.assertEqual(determine_tense_input("They have a car."), ["present_simple_affirmative"])
    def test_psn(self):
        self.assertEqual(determine_tense_input("They don't have a car."), ["present_simple_negative"])
    def test_psn1(self):
        self.assertEqual(determine_tense_input("They Don't have a car."), ["present_simple_negative"])
    def test_psi(self):
        self.assertEqual(determine_tense_input("Do they have a car?"), ["present_simple_interrogative"])
    def test_pca(self):
        self.assertEqual(determine_tense_input("He is reading now."), ["present_continuous_affirmative"])
    def test_pcn(self):
        self.assertEqual(determine_tense_input("He isn't reading now."), ["present_continuous_negative"])
    def test_pci(self):
        self.assertEqual(determine_tense_input("Is he reading now?"), ["present_continuous_interrogative"])
    def test_pasa(self):
        self.assertEqual(determine_tense_input("They saw a movie."), ["past_simple_affirmative"])
    def test_pasn(self):
        self.assertEqual(determine_tense_input("They didn't see a movie."), ["past_simple_negative"])
    def test_pasi(self):
        self.assertEqual(determine_tense_input("Did they see a movie?"), ["past_simple_interrogative"])
    def test_paca(self):
        self.assertEqual(determine_tense_input("It was snowing."), ["past_continuous_affirmative"])
    def test_pacn(self):
        self.assertEqual(determine_tense_input("It wasn't snowing."), ["past_continuous_negative"])
    def test_paci(self):
        self.assertEqual(determine_tense_input("Was it snowing?"), ["past_continuous_interrogative"])
    def test_ppa(self):
        self.assertEqual(determine_tense_input("We have been there."), ["present_perfect_affirmative"])
    def test_ppn(self):
        self.assertEqual(determine_tense_input("We haven't been there."), ["present_perfect_negative"])
    def test_ppi(self):
        self.assertEqual(determine_tense_input("Have we been there?"), ["present_perfect_interrogative"])
    def test_ppca(self):
        self.assertEqual(determine_tense_input("You have been working hard."), ["present_perfect_continuous_affirmative"])
    def test_ppcn(self):
        self.assertEqual(determine_tense_input("You haven't been working hard."), ["present_perfect_continuous_negative"])
    def test_ppci(self):
        self.assertEqual(determine_tense_input("Have you been working hard?"), ["present_perfect_continuous_interrogative"])
    def test_papa(self):
        self.assertEqual(determine_tense_input("They had left for France."), ["past_perfect_affirmative"])
    def test_papn(self):
        self.assertEqual(determine_tense_input("They hadn't left for France."), ["past_perfect_negative"])
    def test_papi(self):
        self.assertEqual(determine_tense_input("Had they left for France?"), ["past_perfect_interrogative"])
        #NLTK tagged 'left' as VBD, whereas it should be VBN: TODO: bug report
    def test_papca(self):
        self.assertEqual(determine_tense_input("She had been waiting for him."), ["past_perfect_continuous_affirmative"])
    def test_papcn(self):
        self.assertEqual(determine_tense_input("She hadn't been waiting for him."), ["past_perfect_continuous_negative"])
    def test_papci(self):
        self.assertEqual(determine_tense_input("Had she been waiting for him?"), ["past_perfect_continuous_interrogative"])
    def test_fsa(self):
        self.assertEqual(determine_tense_input("It will snow this Winter."), ["future_simple_affirmative"])
    def test_fsn(self):
        self.assertEqual(determine_tense_input("It won't snow this Winter."), ["future_simple_negative"])
    def test_fsi(self):
        self.assertEqual(determine_tense_input("Will it snow this Winter?"), ["future_simple_interogative"])
    def test_fca(self):
        self.assertEqual(determine_tense_input("She will be travelling."), ["future_continuous_affirmative"])
    def test_fcn(self):
        self.assertEqual(determine_tense_input("She won't be travelling."), ["future_continuous_negative"])
    def test_fci(self):
        self.assertEqual(determine_tense_input("Will she be travelling?"), ["future_continuous_interrogative"])
    def test_fpa(self):
        self.assertEqual(determine_tense_input("He will have arrived."), ["future_perfect_affirmative"])
    def test_fpn(self):
        self.assertEqual(determine_tense_input("He won't have arrived"), ["future_perfect_negative"])
    def test_fpi(self):
        self.assertEqual(determine_tense_input("Will he have arrived?"), ["future_perfect_interrogative"])
    def test_fpca(self):
        self.assertEqual(determine_tense_input("You will have been working."), ["future_perfect_continuous_affirmative"])
    def test_fpcn(self):
        self.assertEqual(determine_tense_input("You won't have been working."), ["future_perfect_continuous_negative"])
    def test_fpci(self):
        self.assertEqual(determine_tense_input("Will you have been working?"), ["future_perfect_continuous_interrogative"])
    def test_ca(self):
        self.assertEqual(determine_tense_input("I would fly there."), ["conditional_affirmative"])
    def test_cn(self):
        self.assertEqual(determine_tense_input("I wouldn't fly there."), ["conditional_negative"])
    def test_ci(self):
        self.assertEqual(determine_tense_input("Would you fly there?"), ["conditional_interrogative"])
    def test_cca(self):
        self.assertEqual(determine_tense_input("They would be sleeping now."), ["conditional_continuous_affirmative"])
    def test_ccn(self):
        self.assertEqual(determine_tense_input("They wouldn't be sleeping now."), ["conditional_continuous_negative"])
    def test_cci(self):
        self.assertEqual(determine_tense_input("Would they be sleeping now?"), ["conditional_continuous_interrogative"])
    def test_cpa(self):
        self.assertEqual(determine_tense_input("She would have been there."), ["conditional_perfect_affirmative"])
    def test_cpn(self):
        self.assertEqual(determine_tense_input("She wouldn't have been there."), ["conditional perfect_negative"])
    def test_cpi(self):
        self.assertEqual(determine_tense_input("Would she have been there?"), ["conditional_perfect_interrogative"])
    def test_futa(self):
        self.assertEqual(determine_tense_input("She is going to get married."), ["future_be_going_to_affirmative"])
    def test_futn(self):
        self.assertEqual(determine_tense_input("She isn't going to get married."), ["future_be_going_to_negative"])
    def test_futi(self):
        self.assertEqual(determine_tense_input("Is she going to get married?"), ["future_be_going_to_interrogative"])
    
if __name__ == '__main__':
    unittest.main()

