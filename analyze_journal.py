from textblob import TextBlob
import sqlite3



def main():


    conn = sqlite3.connect('./db/db.sqlite3')
    c = conn.cursor()
    c.execute('select date, notes from main_day order by date;')
    notes = c.fetchall()
    conn.close()

    feelings = []

    for i, note in enumerate(notes):

        if i % 100 == 0:
            print i, '/', len(notes)

        testimonial = TextBlob(note[1])
        day = '"{}",{}'.format(note[0], testimonial.sentiment.polarity)
        feelings.append(day)


    with open('outfile.csv', 'wb') as f:
        for feel in feelings:
            f.write(feel)
            f.write('\n')

if __name__ == '__main__':
    main()


#
# print testimonial.sentiment
# print testimonial.sentiment.polarity