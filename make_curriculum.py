import json, random
from pathlib import Path

DATA=[]
def q(prompt,answer,wrong,why):
    opts=list(dict.fromkeys([str(answer)]+[str(x) for x in wrong]))
    assert len(opts)>=3,(prompt,opts)
    random.Random(prompt).shuffle(opts)
    return dict(prompt=prompt,answer=str(answer),options=opts,why=why)
def num(prompt,n,why):
    return q(prompt,n,[n+1,n+2,max(0,n-1) if n else 3],why)
def things(n,word):
    # "1 dot", "3 dots": keeps every sentence grammatical for any number.
    return f'{n} {word}' if n==1 else f'{n} {word}s'
def is_are(n):
    return 'is' if n==1 else 'are'
def add(subject,unit,title,learn,questions,activity):
    n=sum(m['subject']==subject for m in DATA)+1
    DATA.append(dict(id=f'{subject}-{n}',subject=subject,number=n,unit=unit,title=title,learn=learn,questions=questions,activity=activity))

math_units=['Count to 5','Count to 10','Compare and order','Shapes around us','Patterns and positions','Addition to 5','Subtraction to 5','Numbers to 20','Measure and sort','Put it all together']
for i in range(50):
    u=i//5;j=i%5;unit=math_units[u]
    if u==0:
        n=j+1;title=f'Meet number {n}';learn=f'This is number {n}. It tells us how many. Touch each thing once as you count. The last number you say tells how many there are.'
        qs=[num('Count the dots: '+'● '*n,n,f'There {is_are(n)} {things(n,"dot")}. The last number you say tells how many.'),num(f'Which number means {n}?',n,f'The number {n} stands for {things(n,"thing")}.'),num(f'You touch each block and count up to {n}. How many blocks are there?',n,'The last number you say tells how many.')];act=f'Find {things(n,"big toy")} you can hold. Move each one as you count it. Then draw {things(n,"circle")}.'
    elif u==1:
        n=j+6;title=f'Count to {n}';learn=f'Let’s keep counting past 5! Count slowly all the way to {n}. A neat row and a messy pile can have the same number.'
        qs=[num('Count the dots: '+'● '*n,n,f'Count each dot just once. There are {n}.'),num(f'What comes after {n-1}?',n,f'{n-1}, then {n}. They are counting neighbors!'),num(f'You move {n} buttons into a row. How many buttons are there now?',n,'Moving things around does not change how many there are.')];act=f'Make a pile of {n} big toys. Spread them out in a row and count again. Is it still {n}?'
    elif u==2:
        titles=['More and fewer','The same amount','Before and after','Put numbers in order','Compare within 10'];title=titles[j]
        learn=['More means a bigger number. Fewer means a smaller number. Match things in pairs to compare.','Equal groups have the same number. Things can look different and still be equal in number.','The number before is one less. The number after is one more.','Counting numbers go in order: 1, 2, 3, 4, 5, and on and on.','Compare how many things there are, even when one group takes up more space.'][j]
        same='the same'
        specs=[ [('Which is more: 3 or 5?',5,[3,same],'5 is more than 3. We say 5 later when we count.'),('Which is fewer: 2 or 4?',2,[4,same],'2 is fewer than 4. We say 2 first when we count.'),('One group has 6 dots. Another group has 4 dots. Which number is more?',6,[4,same],'6 is more than 4. Match the dots in pairs and 2 are left over.')],
                [('Tom has 4 apples. Ana has the same number. How many apples does Ana have?',4,[3,5],'The same number means equal. Tom has 4, so Ana has 4.'),('A tower has 7 blocks. Which tower has the same number?','7 blocks',['6 blocks','8 blocks'],'7 and 7 are equal.'),('Two plates each have 5 grapes. Does one plate have more?','No, they are equal',['Yes, the first plate','Yes, the second plate'],'5 and 5 are the same number, so neither plate has more.')],
                None,
                None,
                [('Which is fewer: 9 or 7?',7,[9,same],'7 is fewer than 9. We say 7 first when we count.'),('Which is more: 8 or 10?',10,[8,same],'10 is more than 8. We say 10 later when we count.'),None] ]
        if j==2:qs=[num('What comes before 5?',4,'4 comes just before 5. It is one less.'),num('What comes after 7?',8,'8 comes just after 7. It is one more.'),num('What comes before 3?',2,'2 comes just before 3. It is one less.')]
        elif j==3:qs=[num('Fill the gap: 2, 3, __, 5',4,'2, 3, 4, 5. The number 4 fills the gap.'),q('Which number comes first when you count?',6,[8,9],'We count 6, 7, 8, 9. So 6 comes first.'),num('Fill the gap: 6, 7, __, 9',8,'6, 7, 8, 9. The number 8 fills the gap.')]
        else:
            qs=[q(*x) for x in specs[j] if x]
            if j==4:qs.append(num('Which number is between 4 and 6?',5,'4, 5, 6. The number 5 is in the middle.'))
        act='Make two groups of toys. Match one from each group. Tell a grown-up which group has more, fewer, or the same.'
    elif u==3:
        title=['Circles','Squares','Triangles','Rectangles','Shapes in the world'][j]
        learn=['A circle has a curved edge and no corners.','A square has 4 equal straight sides and 4 corners.','A triangle has 3 straight sides and 3 corners.','A rectangle has 4 straight sides and 4 square corners. Some rectangles have two longer sides.','Shapes stay the same when we turn them. Look at sides and corners to name a shape.'][j]
        specs=[ [('Which has no corners?','circle',['square','triangle']),('A round clock face looks like a...','circle',['triangle','rectangle']),('How many corners does a circle have?',0,[3,4])], [('How many sides does a square have?',4,[3,5]),('Which shape has 4 equal sides?','square',['circle','triangle']),('A square has how many corners?',4,[0,3])], [('How many sides does a triangle have?',3,[2,4]),('Which shape has 3 corners?','triangle',['square','circle']),('A triangle turned sideways is still a...','triangle',['circle','square'])], [('How many corners does a rectangle have?',4,[0,3]),('A door usually looks like a...','rectangle',['circle','triangle']),('Which shape can have 2 long and 2 short sides?','rectangle',['circle','triangle'])], [('Which shape matches a round plate?','circle',['square','triangle']),('Which has 3 straight sides?','triangle',['rectangle','circle']),('A turned square is still a...','square',['circle','triangle'])] ]
        qs=[q(p,a,w,learn) for p,a,w in specs[j]];act='Draw this shape. Find something at home with a similar shape and tell a grown-up about its sides.'
    elif u==4:
        title=['Repeating AB patterns','Repeating AAB patterns','Repeating ABC patterns','Where is it?','Follow a pattern'][j]
        learn=['A pattern repeats a part. In red, blue, red, blue, the repeating part is red, blue.','Some patterns repeat three items: clap, clap, tap. Find the whole repeating part.','An ABC pattern repeats three different items in the same order.','Position words tell where things are: above, below, inside, outside, and between.','Find the repeating part, then say what comes next. Use actions or objects to make patterns.'][j]
        specs=[ [('red, blue, red, blue, ...','red',['blue','green']),('clap, tap, clap, tap, ...','clap',['tap','jump']),('circle, square, circle, square, ...','circle',['square','triangle'])], [('clap, clap, tap, clap, clap, ...','tap',['clap','hop']),('red, red, blue, red, red, ...','blue',['red','yellow']),('circle, circle, square, circle, ...','circle',['square','triangle'])], [('red, blue, green, red, blue, ...','green',['blue','red']),('clap, tap, hop, clap, ...','tap',['hop','clap']),('1, 2, 3, 1, 2, ...','3',['1','2'])], [('A toy in a closed box is...','inside',['outside','above']),('A book under the table is...','below',['above','inside']),('In the row cat, dog, hen, the dog is...','between',['above','below'])], [('1, 2, 1, 2, ...','1',['2','3']),('A, A, B, A, A, ...','B',['A','C']),('tap, hop, clap, tap, hop, ...','clap',['tap','hop'])] ]
        qs=[q(p,a,w,learn) for p,a,w in specs[j]];act='Make a repeating pattern with claps and taps. Ask a grown-up to continue it.'
    elif u in [5,6]:
        pairs=[[(1,1),(2,1),(1,2)],[(2,2),(3,1),(1,3)],[(3,2),(4,1),(2,3)],[(0,3),(2,0),(0,5)],[(1,4),(2,2),(3,2)]] if u==5 else [[(2,1),(3,1),(4,1)],[(3,2),(4,2),(5,2)],[(4,3),(5,3),(5,4)],[(3,0),(4,4),(5,0)],[(5,1),(5,5),(4,2)]]
        title=(['Join small groups','Make 4','Make 5','Adding zero','Addition stories'] if u==5 else ['Take away one','Take away two','Take away more','Zero and all','Subtraction stories'])[j]
        learn='Addition joins groups. Count all the objects to find the total. Adding zero keeps the number the same.' if u==5 else 'Subtraction takes objects away. Count what is left. Taking away zero keeps the number the same.'
        qs=[]
        for a,b in pairs[j]:
            n=a+b if u==5 else a-b;op='+' if u==5 else '-'
            p=f'{a} {op} {b} = ?' if j<4 else (f'You have {things(a,"block")}. You get {b} more. How many blocks do you have now?' if u==5 else f'You have {things(a,"block")}. You put away {b}. How many blocks are left?')
            why=(f'{a} {op} {b} = {n}. ' if j<4 else '')+(f'{a} and {b} more make {n}.' if u==5 else f'Start with {a}. Take away {b}. {n} {is_are(n)} left.')
            qs.append(num(p,n,why))
        act='Use 5 big toys. Act out each number sentence. Draw one of your stories.'
    elif u==7:
        title=['Meet 11 and 12','Meet 13 and 14','Meet 15 and 16','Meet 17 and 18','Meet 19 and 20'][j];n=11+2*j
        learn=f'A group of ten helps us count bigger numbers. {n} is 10 and {n-10} more. {n+1} is 10 and {n-9} more.'
        qs=[num(f'10 and {n-10} more make...',n,learn),num(f'What comes after {n}?',n+1,learn),num(f'Fill the gap: {n-1}, __, {n+1}',n,learn)];act=f'Draw 10 dots in two rows of 5. Add {n-10} more. Count them all. Did you get {n}?'
    elif u==8:
        title=['Longer and shorter','Taller and shorter','Heavier and lighter','Sort by a rule','Measure with blocks'][j]
        learn=['Compare length by lining up one end of each object.','Compare height from the same starting level.','Heavy and light describe weight. Bigger objects are not always heavier.','Sort objects by one rule, such as color, shape, or size.','Use equal-sized units with no gaps or overlaps to measure.'][j]
        specs=[ [('A ribbon is 5 blocks long. Another is 3 blocks long. Which is longer?','5 blocks',['3 blocks','same length']),('Which is shorter: 2 blocks or 6 blocks long?','2 blocks',['6 blocks','same length']),('How should you line up pencils to compare length?','Match one end',['Use different starts','Hide one pencil'])], [('A tower is 4 blocks tall. Another is 7 blocks tall. Which is taller?','7 blocks',['4 blocks','same height']),('Which tower is shorter: 3 or 5 blocks tall?','3 blocks',['5 blocks','same height']),('To compare height, start both towers...','on the same level',['at different levels','upside down'])], [('A full water bottle is usually heavier than...','an empty bottle',['a full bucket','a large desk']),('Which is usually lighter?','a feather',['a brick','a full bucket']),('Does bigger always mean heavier?','No',['Yes','Always'])], [('Sort by color: where does a red button go?','with red objects',['with blue objects','with all circles']),('Sort by shape: a round lid goes with...','circles',['triangles','squares']),('Which is a sorting rule?','same color',['close your eyes','count backwards'])], [('A pencil covers 6 equal blocks. Its length is...','6 blocks',['3 blocks','8 blocks']),('Measuring blocks should have...','no gaps',['big gaps','overlaps']),('Which units are best for comparing lengths?','equal-sized blocks',['mixed-sized blocks','random gaps'])] ]
        qs=[q(p,a,w,learn) for p,a,w in specs[j]];act='Compare two safe objects at home. Describe them using the words from this lesson.'
    else:
        title=['Add within 10','Subtract within 10','Make ten','Picture data','Math explorer'][j]
        learn=['Use objects or count on to add within 10.','Take away objects to subtract within 10.','Two groups can join to make ten. A ten-frame has two rows of five spaces.','Count each group in a picture chart to compare information.','Use counting, adding, comparing, and patterns to solve everyday problems.'][j]
        if j==0:qs=[num(f'{a} + {b} = ?',a+b,f'{a} + {b} = {a+b}.') for a,b in [(5,2),(4,4),(6,3)]]
        elif j==1:qs=[num(f'{a} - {b} = ?',a-b,f'{a} - {b} = {a-b}.') for a,b in [(7,2),(8,3),(10,4)]]
        elif j==2:qs=[num(f'{a} + __ = 10',10-a,f'{a} and {10-a} make 10.') for a in [5,7,9]]
        elif j==3:qs=[q('Chart: cats ● ● ●; dogs ● ●. Which has more?','cats',['dogs','equal'],'Cats have 3; dogs have 2.'),num('Chart: cats ● ● ●; dogs ● ●. How many pets altogether?',5,'3 + 2 = 5.'),num('Chart: apples ● ● ● ●; pears ● ●. How many more apples?',2,'Match pairs. Two apples are left over.')]
        else:qs=[num('You have 4 red blocks and 3 blue blocks. How many in all?',7,'4 + 3 = 7.'),num('You have 9 crayons and lend 2. How many stay with you?',7,'9 - 2 = 7.'),q('What comes next: circle, square, circle, square?','circle',['square','triangle'],'The repeating part is circle, square.')]
        act='Make up your own math story with big toys. Ask a grown-up to solve it, then show your answer.'
    add('math',unit,title,learn,qs,act)

# Each row: title | teaching | prompt ~ correct ~ wrong 1 ~ wrong 2 (three questions).
english='''
Meet A and a|Capital A and small a are the same letter. In apple, a has its short sound.|Which is small A?~a~b~d|Which is capital a?~A~B~C|Which word starts like apple?~ant~sun~dog
Meet B and b|B and b are the same letter. Listen for b at the start of ball.|Which is small B?~b~d~p|Which is capital b?~B~D~P|Which word starts like ball?~bat~cat~sun
Meet M and m|M and m are the same letter. M makes the sound at the start of map.|Which is small M?~m~n~w|Which is capital m?~M~N~W|Which starts like map?~moon~dog~sun
Meet S and s|S and s are the same letter. S makes the sound at the start of sun.|Which is small S?~s~c~z|Which is capital s?~S~C~Z|Which starts like sun?~sock~map~dog
Letter review A B M S|Say letter names and match capital letters to small letters.|Which pair matches?~A a~A b~A s|Which pair matches?~M m~M s~M b|Which starts with s?~sun~bat~map
Meet T and t|T and t are the same letter. Listen for t in top.|Which is small T?~t~f~l|Which is capital t?~T~F~L|Which starts like top?~tap~map~sun
Meet C and c|C and c are the same letter. In cat, c makes a hard sound like k.|Which is small C?~c~e~o|Which is capital c?~C~G~O|Which starts like cat?~cup~sun~map
Meet D and d|D and d are the same letter. Listen for d at the start of dog.|Which is small D?~d~b~p|Which is capital d?~D~B~P|Which starts like dog?~dig~cat~sun
Meet F and f|F and f are the same letter. Listen for f in fish.|Which is small F?~f~t~l|Which is capital f?~F~T~L|Which starts like fish?~fan~dog~map
More letter partners|Capital and small letters can look different. Match them by name.|Which pair matches?~T t~T f~T c|Which pair matches?~D d~D b~D p|Which pair matches?~F f~F t~F s
Short a|Listen to the middle sound in cat, map, and tap. It is short a.|Fill the middle: c_t (cat).~a~i~o|Which has the same middle sound as cat?~map~sit~sun|Fill the middle: t_p (tap).~a~e~u
Short i|Listen to the middle sound in sit, pin, and dig. It is short i.|Fill the middle: s_t (sit).~i~a~o|Which has the same middle sound as sit?~pin~cat~dog|Fill the middle: d_g (dig).~i~a~u
Short o|Listen to the middle sound in pot, top, and hot. It is short o.|Fill the middle: p_t (pot).~o~a~i|Which has the same middle sound as pot?~top~map~sit|Fill the middle: h_t (hot).~o~e~u
Short e|Listen to the middle sound in hen, pen, and bed. It is short e.|Fill the middle: h_n (hen).~e~a~i|Which has the same middle sound as hen?~pen~sun~cat|Fill the middle: b_d (bed).~e~i~o
Short u|Listen to the middle sound in sun, cup, and bug. It is short u.|Fill the middle: s_n (sun).~u~a~i|Which has the same middle sound as sun?~cup~cat~hen|Fill the middle: b_g (bug).~u~e~o
First sounds|Listen for the very first sound in a word. A grown-up can help say the words.|Which begins with m?~mat~cat~dog|Which begins with t?~top~sun~map|Which begins with f?~fan~dog~cat
Last sounds|Listen to the last sound of a word. Say the word slowly.|Which letter is at the end of cat?~t~c~a|Which letter is at the end of map?~p~m~a|Which letter is at the end of sun?~n~s~u
Clap word parts|Syllables are spoken word parts. Clap once for each part: sun has one; rabbit has two.|How many claps for sun?~1~2~3|How many claps for rabbit?~2~1~3|How many claps for banana?~3~1~2
Hear rhyming words|Rhyming words have the same ending sound. Cat and hat rhyme.|Which rhymes with cat?~hat~sun~dog|Which rhymes with pen?~hen~map~cup|Which rhymes with bug?~rug~cat~pin
Sound detective|Listen for first, middle, and last sounds. Some words rhyme even with different first sounds.|Which begins like dog?~dig~sun~map|Which ends like cat?~hat~dog~sun|Which has short i?~sit~cup~bed
Blend with a|Say each sound slowly, then slide them together: m-a-t makes mat.|Blend m-a-t.~mat~map~sat|Blend c-a-t.~cat~cot~cut|Blend s-a-t.~sat~sit~sun
Blend with i|Slide three sounds together: s-i-t makes sit. Listen to every sound.|Blend s-i-t.~sit~sat~set|Blend p-i-n.~pin~pan~pen|Blend d-i-g.~dig~dog~dug
Blend with o|Say the sounds in order. p-o-t makes pot.|Blend p-o-t.~pot~pat~pet|Blend t-o-p.~top~tap~tip|Blend h-o-t.~hot~hat~hit
Blend with e|Say the sounds in order. p-e-n makes pen.|Blend p-e-n.~pen~pin~pan|Blend h-e-n.~hen~hat~hit|Blend b-e-d.~bed~bad~bid
Blend with u|Say the sounds in order. s-u-n makes sun.|Blend s-u-n.~sun~son~sat|Blend c-u-p.~cup~cap~cop|Blend b-u-g.~bug~bag~big
Build a word|Listen to a word, then choose its letters in order.|Which spells cat?~c-a-t~t-a-c~c-t-a|Which spells sun?~s-u-n~n-u-s~s-n-u|Which spells pin?~p-i-n~n-i-p~p-n-i
Change the first sound|Change one sound to make a new word. Cat becomes hat when c changes to h.|Change c in cat to h.~hat~hot~hit|Change m in map to t.~tap~top~tip|Change p in pin to f.~fin~fan~fun
Change the middle sound|Changing a vowel changes the middle sound and can make a new word.|Change a in cat to o.~cot~cut~cap|Change i in pin to e.~pen~pan~pit|Change o in hot to a.~hat~hit~hut
Change the last sound|Listen carefully to the end. Change the last sound and read the new word.|Change t in cat to p.~cap~cup~cot|Change n in pin to g.~pig~pit~pan|Change p in map to t.~mat~met~mop
Word builder review|Sound out each letter. Check the first, middle, and last sounds.|Which word is c-u-p?~cup~cap~cop|Which word starts m and ends p?~map~mat~tap|Which word rhymes with sit?~hit~hat~hot
The at family|Cat, hat, mat, and sat share the ending at. Change the first sound to read a new word.|Which belongs with cat and mat?~hat~hot~hit|Fill the word: m + at.~mat~met~mit|Which rhymes with sat?~bat~bet~bit
The an family|Can, fan, man, and pan share the ending an.|Which belongs with can and man?~fan~fin~fun|p + an makes...~pan~pin~pen|Which rhymes with man?~can~cup~cat
The in family|Pin, fin, and bin share the ending in.|Which rhymes with pin?~fin~fan~fun|b + in makes...~bin~bun~ban|Which belongs to the in family?~win~wet~wag
The og and un families|Dog and log rhyme. Sun and run rhyme. Listen to each ending.|Which rhymes with dog?~log~leg~lag|Which rhymes with sun?~run~ran~red|Which ends with og?~fog~fig~fan
Word family review|The ending sounds help us read and rhyme. Look carefully at the vowel.|Which rhymes with fan?~pan~pin~pen|Which rhymes with bin?~fin~fun~fan|Which rhymes with log?~dog~dig~dug
Meet I and a|I is a word for yourself and is always capitalized. A can mean one, as in a cat.|Which word means yourself?~I~a~the|Fill: I see __ cat.~a~I~we|Which is the correct word for yourself?~I~i~A
Meet the and see|The points to a particular thing. See tells about looking. Read: I see the cat.|Fill: I __ the cat.~see~the~a|Which word says “the”?~the~see~I|In I see the dog, what do I see?~dog~cat~sun
Meet my and like|My tells something belongs to me. Like tells about something I enjoy.|Fill: This is __ bag. It belongs to me.~my~see~the|Fill: I __ cats. I enjoy them.~like~the~my|In I like my dog, whose dog is it?~mine~Sam's~nobody's
Meet we and can|We means me and others. Can tells what someone is able to do.|Which means me and others?~we~I~a|Fill: We __ run.~can~the~my|In We can hop, what can we do?~hop~sit~dig
Little word review|Use small words to help read a sentence. Read slowly and ask what it means.|Fill: I __ the sun.~see~my~the|Fill: __ can sit. (Me and a friend.)~We~A~The|Fill: I like __ cat. It belongs to me.~my~can~see
Words make sentences|A sentence gives a whole idea. Spaces separate words. A sentence starts with a capital letter.|Which is a whole sentence?~The cat can sit.~cat the~can|How many words in I see a cat?~4~3~5|A sentence starts with...~a capital letter~a comma~a small letter always
End marks|A period ends a telling sentence. A question mark ends a question.|Choose the mark: The cat can sit_~.~?~,|Choose the mark: Can you hop_~?~.~,|Which asks a question?~Can we run?~We can run.~I see a cat.
Read about Sam|Read together: Sam has a cat. The cat sits on a mat. Sam pats the cat.|Who has a cat?~Sam~Ben~Meg|Where does the cat sit?~on a mat~in a cup~on a bus|What does Sam do?~pats the cat~feeds a fish~rides a bus
Read about a pet|Read together: Ben has a dog. The dog can run. Ben and the dog run in the park.|What pet does Ben have?~dog~cat~fish|What can the dog do?~run~read~write|Where do they run?~park~kitchen~bed
Story order|Read together: Meg puts on a hat. Then Meg goes outside. Last, Meg waves to Dad.|What happens first?~puts on a hat~waves to Dad~goes outside|What happens next?~goes outside~takes a nap~waves first|What happens last?~waves to Dad~puts on a hat~eats lunch
Describe with words|Describing words tell more about a thing: a red ball, a soft sock, a big dog.|Which word describes the ball in a red ball?~red~a~ball|Which describes how a blanket feels?~soft~runs~jumps|Which describes size?~big~cat~see
Action words|Action words tell what someone does. Hop, run, sit, and clap are actions.|Which is an action?~hop~hat~red|In The dog runs, what is the action?~runs~dog~the|Fill: I can __ my hands.~clap~red~hat
Build a sentence|Put words in order to tell a whole idea. Start with a capital and end with a mark.|Put in order: can / I / hop.~I can hop.~Hop I can.~Can hop I.|Which sentence is written correctly?~The cat sits.~the cat sits~cat The sits|Choose a complete idea.~We can run.~can we~the red
Think about a story|Read together: A cup tips. Water spills on the table. Jo gets a cloth and wipes the table dry.|What spilled?~water~sand~milk|Why did Jo get a cloth?~to wipe the water~to feed a pet~to wear a hat|What happens after Jo wipes?~the table is dry~the cup fills itself~it snows
My reading celebration|Read together: I see a red hen. The hen can run. We like the hen. Tell a grown-up what you read.|What animal is in the story?~hen~dog~cat|What color is the hen?~red~blue~green|What can the hen do?~run~write~read
'''
science='''
Look closely|Scientists look closely and describe what they notice. An observation is something you notice with your senses.|Which is an observation?~The leaf is green.~The leaf is magic.~The leaf wants lunch.|What helps you look closely?~eyes~elbows~knees|Which describes a ball?~round~tomorrow~yesterday
Ask a question|A question helps us learn more. Scientists ask questions they can explore.|Which is a question?~Is this leaf smooth?~This leaf is green.~I have a leaf.|Which could you explore at home?~Which sock is softer?~Can a toy dream?~What does a star wish?|What can you do after asking?~look and explore~just guess~forget about it
Sort what you see|You can group things by a feature you can observe, such as color, shape, or texture.|Sort by color: a red block goes with...~red things~blue things~all circles|Sort by shape: a round lid goes with...~circles~triangles~squares|Which is a feature you can observe?~color~a toy's wishes~a rock's dreams
Draw your observations|A drawing can record what you notice. Add details you can actually see.|What belongs in a leaf drawing?~its edges and lines~imaginary wings~a secret wish|Why draw an object?~to record what you notice~to make it grow~to change its weight|What makes a useful observation?~looking carefully~keeping your eyes closed~making things up
Be an observer|Look, ask, sort, and record. Share what you noticed with a grown-up.|You notice 3 leaves. What can you record?~draw 3 leaves~draw 9 leaves~draw no leaves|Which uses observation?~noticing a rough edge~guessing without looking~pretending it talks|What can you share?~what you noticed~only guesses~nothing at all
Eyes help us see|Our eyes help us see colors, shapes, and movement. Use light to look at objects.|Which helps you see?~eyes~ears~tongue|What can you notice by looking?~color~taste~smell|What helps you see a book clearly?~enough light~a closed box~closed eyes
Ears help us hear|Our ears help us hear sounds. Sounds may be loud or quiet.|Which helps you hear?~ears~eyes~nose|Which can you hear?~a bell ringing~the color red~a smooth surface|Which describes a sound?~quiet~square~purple
Nose helps us smell|Our nose helps us smell. Only explore familiar safe smells with a grown-up.|Which helps you smell?~nose~knees~eyes|Which sense notices a flower's scent?~smell~hearing~sight|Who helps choose safe things to smell?~a grown-up~a toy~a picture
Taste and touch|The tongue helps us taste food. Skin helps us feel texture and temperature. Only taste food from a grown-up.|Which helps you taste?~tongue~ears~eyes|Which describes texture?~rough~blue~loud|What is safe to taste?~food a grown-up gives you~unknown liquid~soap
Use your senses|Different senses give different information. We do not need to taste things to learn about them.|How do you notice a soft sock?~touch~hearing~taste|How do you notice a bird's song?~hearing~taste~touch|How do you notice a yellow cup?~sight~smell~hearing
Hard and soft|Materials can feel hard or soft. Describe what your hands notice.|Which usually feels soft?~a sock~a stone~a metal spoon|Which usually feels hard?~a spoon~a pillow~a blanket|Which sense checks softness?~touch~hearing~smell
Smooth and rough|A smooth surface has few bumps. A rough surface has bumps or uneven parts.|Which often feels rough?~tree bark~a glass surface~a smooth spoon|Which often feels smooth?~a plastic spoon~rough bark~coarse sandpaper|Rough describes...~texture~color~sound
Materials around us|Objects are made of materials such as wood, metal, plastic, cloth, and paper.|A paper page is made of...~paper~metal~stone|A cotton sock is made of...~cloth~glass~metal|A steel spoon is made of...~metal~paper~cloth
Bend and stretch|Some materials bend easily. Some stretch and spring back. Others are stiff.|Which bends easily?~a piece of cloth~a thick stone~a brick|Stretch means...~pull to make longer~change color~make colder|Which is usually stiff?~a wooden block~a sock~a scarf
Choose a material|Choose materials for what you need. Different materials have different useful features.|For a soft pillow cover, choose...~cloth~stone~metal|For a page to draw on, choose...~paper~a brick~a spoon|Why choose a material?~its features fit the job~all materials are identical~color is the only feature
Living and nonliving|Living things grow and need resources such as water, air, or food. Plants and animals are living.|Which is living?~a tree~a chair~a rock|Which is nonliving?~a toy car~a dog~a flower|Which can grow as a living thing?~a seedling~a spoon~a plastic cup
Needs of living things|Animals need food, water, air, and a suitable place to live. Plants need resources too.|What does a dog need?~water~a television~a phone|What do animals need to breathe?~air~toys~paper|Which is a need for an animal?~food~crayons~a hat
Plants are living|Plants grow. Most green plants use light, water, and air to make food. They need room to grow.|Which is a plant?~grass~a rock~a spoon|What helps a green plant make food?~light~a toy~a book|What do roots take in from the soil?~water~music~plastic
Animals are living|Animals need food and water. Animals can move in different ways and grow as they develop.|Which is an animal?~a fish~a tree~a chair|Which does a fish do?~swim~read~write|Why does an animal eat?~to get energy and grow~to become a toy~to change into a rock
Care for living things|A grown-up can help care for plants and pets. Give the right food, water, and space.|How can you help a houseplant?~water as needed~cover it in soap~pull all its leaves|How can you help a pet?~give proper care with an adult~offer unknown food~hide its water|Who helps decide what a pet needs?~a grown-up~a toy~a crayon
Parts of a plant|Roots, stems, and leaves are parts of many plants. Each part has a job.|Which part is usually below the soil?~roots~leaves~flowers|Which part holds leaves up?~stem~roots only~a toy|Which part is often green and uses light?~leaves~a pot~a label
Seeds can grow|A seed can grow into a plant under the right conditions. Many seeds need water, air, and suitable warmth.|What can a seed become?~a plant~a spoon~a stone|What helps many seeds start growing?~water~soap~paint|Does every dry seed grow at once?~No~Yes always~Only if painted
Roots and stems|Roots anchor a plant and take in water. A stem supports the plant and carries water.|What helps anchor a plant?~roots~a leaf tip~a flower petal|What carries water up a plant?~stem~a toy~a label|Where do roots often grow?~in soil~only in the sky~on a book page
Leaves and flowers|Leaves help green plants make food using light. Many plants have flowers that help make seeds.|What do leaves use to help make food?~light~plastic~music|What can many flowers help make?~seeds~spoons~rocks|Are all plants the same shape?~No~Yes always~Only squares
Watch a plant change|Record changes as a plant grows. Compare it over several days with a grown-up.|What can you record each day?~number of leaves~its wishes~its dreams|How can you compare growth?~draw it on different days~look once and forget~hide all records|A new leaf is a sign of...~growth~turning to stone~becoming a toy
Animal body parts|Animals have body parts that help them live. Wings, fins, and legs help with movement.|A fish uses fins to help...~swim~write~read|A bird's wings can help it...~fly~type~paint|A dog's legs help it...~walk~make seeds~grow leaves
Animal coverings|Fur, feathers, and scales cover different animals. Coverings can help protect their bodies.|What covers most birds?~feathers~fur~paper|What covers many fish?~scales~cloth~feathers|What covers a cat?~fur~leaves~metal
Animal homes|A habitat is a place where an animal finds what it needs. Different animals live in different habitats.|A fish's habitat needs...~water~dry paper~a cupboard|A pond is a habitat for...~a frog~a house cat only~a wooden chair|What should a habitat provide?~food and shelter~only toys~only paint
Animals and food|Animals eat different foods. Some eat plants, some eat other animals, and some eat both.|A rabbit often eats...~plants~metal~plastic|An animal needs food for...~energy~becoming a rock~making paper|Do all animals eat the same food?~No~Yes always~Only toys
Animal young|Young animals grow into adults of their own kind. A kitten grows into a cat.|A kitten grows into a...~cat~dog~tree|A puppy grows into a...~dog~fish~flower|What do young animals do as they develop?~grow~turn into toys~become rocks
Sunny and cloudy|Weather describes what the air and sky are like now. Clouds can cover some or all of the sky.|A sky with many clouds is...~cloudy~clear~a material|What gives daylight?~the Sun~a tree~a rock|What can you observe to describe weather?~sky and air~a toy's wishes~a book's dreams
Rain and snow|Rain is liquid water falling from clouds. Snow is made of ice crystals and can fall in cold conditions.|Rain is...~liquid water~paper~sand|Snow is made of...~ice crystals~plastic~leaves|Where does rain fall from?~clouds~a bookshelf~the ground upward
Wind moves things|Wind is moving air. We can notice it by what it moves, such as leaves or a flag.|Wind is moving...~air~stone~paper only|Which can show wind?~a fluttering flag~a closed book~a still wall|What might wind move?~leaves~a large building~the Moon
Dress for weather|Choose clothing for the weather with a grown-up. Keep dry in rain and warm in cold weather.|What helps in rain?~a raincoat~paper clothes~no coat ever|What helps in cold weather?~a warm coat~only a swimsuit~wet socks|Before going out, check...~the weather~a toy's color~a book title only
Keep a weather chart|Observe weather each day. A chart helps you compare sunny, rainy, cloudy, or windy days.|What should you record on a weather chart?~today's weather~only guesses~your pet's name|What helps compare days?~a record for each day~no record~one random drawing|If you observe rain, draw...~a rain symbol~a sunny-only symbol~a toy car
Land and water|Earth has land and water. Soil, sand, and rocks are found on land. Lakes and oceans hold water.|Which is a body of water?~a lake~a hill~a rock|Which is land?~a hill~an ocean~a pond|An ocean contains...~water~only soil~only paper
Rocks and soil|Rocks come in many sizes and textures. Soil is a mixture that can support plants and small living things.|What can you compare in rocks?~size and texture~their wishes~their favorite songs|What can many plants grow in?~soil~a metal spoon~a plastic lid alone|Are all rocks identical?~No~Yes always~Only if wet
Day and night|Earth turns. Our part has day when it faces the Sun, and night when it faces away.|During day, our part of Earth faces...~the Sun~a lamp in a room~a tree|At night, our part faces...~away from the Sun~always toward the Sun~inside the Sun|What turns to make day and night?~Earth~a book~a cloud only
Sun Moon and stars|The Sun is a star. The Moon reflects sunlight. Other stars are easier to see when the sky is dark.|The Sun is a...~star~plant~rock on Earth|The Moon looks bright because it reflects...~sunlight~its own fire~paper|When are other stars usually easier to see?~at night~in bright daylight~inside a closed box
Care for Earth|We can reduce waste, reuse items, and save water with a grown-up. Follow local recycling rules.|Which saves water?~turning off a running tap~leaving it running~spilling clean water|Which is reusing?~using a box again~throwing away a good box~breaking a toy|Who helps check recycling rules?~a grown-up~a toy~a leaf
Push and pull|A push moves something away from you. A pull brings it toward you. Forces can change motion.|Moving a toy away with your hand is a...~push~pull~taste|Bringing a wagon toward you is a...~pull~push~smell|A push or pull can change...~motion~a toy into a plant~paper into water
Fast and slow|Objects can move at different speeds. Compare how far they travel in the same time.|Which is usually faster?~a running child~a slowly crawling snail~a still toy|A toy that does not move is...~still~fast~flying|To compare speed fairly, use...~the same time interval~different random times~no observation
Light and shadows|A shadow forms when an object blocks light. We can explore shadows using a flashlight with a grown-up.|What is needed for a shadow?~light and an object~only sound~only smell|An object makes a shadow by...~blocking light~making water~growing roots|What can provide light?~a flashlight~a sock~a closed box
Making sounds|Sounds begin when something vibrates, or moves back and forth. Gentle tapping and humming can make sounds.|What begins a sound?~vibration~color~shape alone|Which can make a sound?~humming~looking at red~smelling a flower|How should you explore sound at home?~gently with a grown-up~shout into someone's ear~bang breakable objects
Explore magnets|Magnets attract some metals, such as iron. They do not attract every material. Explore only large enclosed magnets with a grown-up.|A magnet can attract...~some metals~every material~paper always|Does a magnet attract all metals?~No~Yes always~Only cloth|Who should help explore magnets?~a grown-up~a toy~a picture
Predict and check|A prediction is what you think will happen. Then observe what really happens. It is okay if your prediction differs.|A prediction is...~what you think will happen~a certain fact always~a made-up observation|What do you do after predicting?~check by observing~hide the result~change your record to match|If the result differs, you can...~learn from it~pretend it did not happen~stop being curious
Try a fair comparison|Change one thing when comparing. Keep other things the same so you can learn what made a difference.|To compare two toy ramps, use...~the same toy~different toys and ramps each time~no toy|What should you change at a time?~one thing~everything~your record after testing|Why keep other things the same?~to make a fair comparison~to hide results~to stop observing
Float and sink|An object that floats stays at the water surface. An object that sinks goes down. A grown-up must help with a small bowl of water.|An object at the water surface is...~floating~sinking~flying|An object going to the bottom is...~sinking~floating~growing|How do you find out if a safe object floats?~test with a grown-up~guess and never check~only look at its color
Watch water change|Water can freeze into ice. Ice can melt into liquid water when it warms. Observe with a grown-up; do not use hot water.|Frozen water is...~ice~sand~paper|Ice that warms can...~melt~grow leaves~turn into cloth|Melting ice becomes...~liquid water~a rock~a leaf
My science celebration|Ask a question, predict, observe, and record. Explain what you found using your observations.|What comes after testing a prediction?~observe and record~erase real results~only guess again|Which is evidence?~what you observed~a toy's wish~an imagined result|What can you tell a grown-up?~what happened and what you noticed~only what you hoped~nothing about the result
'''
eng_units=['Letter beginnings','More letter partners','Short vowel sounds','Listen to words','Blend and read','Build and change words','Word families','Helpful little words','Read little stories','Speak and write']
sci_units=['Observe and ask','Our five senses','Explore materials','Living things','Growing plants','Animal explorers','Weather watchers','Earth and sky','Care and motion','Investigate and celebrate']
eng_activities=['Write the capital and small letter. Find it on a book cover.','Write the letter pair and say a word that starts with its sound.','Say three words from the lesson. Draw one and label it with help.','Say the words slowly with a grown-up. Clap or point to the sounds.','Read three lesson words aloud. Copy one and draw its meaning.','Use paper letter cards to build and change a lesson word.','Say two rhyming words. Draw and label one with help.','Say a sentence using a lesson word. A grown-up can write it for you.','Retell the lesson story. Draw something that happened.','Tell a whole sentence about your day. Write or dictate it, then draw it.']
sci_activities=['Look at a safe object. Draw it and tell a grown-up two details.','With a grown-up, explore a safe familiar object. Describe it using a sense.','Compare a sock, spoon, and book. Describe the material and how it feels.','Look for a plant or animal with a grown-up. Tell what it needs.','Look at a plant with a grown-up. Draw its parts or changes.','Draw an animal. Tell a grown-up about its body, food, or habitat.','Look outside with a grown-up. Draw the weather and describe what you notice.','Draw something from land, water, or the sky. Explain one lesson idea.','Find one way to care for Earth or show movement with a safe toy.','With a grown-up, predict how a toy will move with a gentle push. Try it and draw what happened.']
for subject,raw,units,activities in [('english',english,eng_units,eng_activities),('science',science,sci_units,sci_activities)]:
    rows=[r for r in raw.strip().splitlines() if r.strip()];assert len(rows)==50,(subject,len(rows))
    for i,row in enumerate(rows):
        title,learn,*items=row.split('|');assert len(items)==3,title
        questions=[]
        for item in items:
            p,a,w1,w2=item.split('~');questions.append(q(p,a,[w1,w2],learn))
        add(subject,units[i//5],title,learn,questions,activities[i//5])
assert len(DATA)==150
for subject in ['math','english','science']:
    mods=[m for m in DATA if m['subject']==subject]
    for i,m in enumerate(mods):
        if i:
            # Mix recent and earlier skills, preserving each review question's provenance.
            previous=[mods[i-1],mods[max(0,i-5)]]
            m['review']=[dict(p['questions'][(i+k)%3],source=p['title'],sourceId=p['id']) for k,p in enumerate(previous)]
        else:m['review']=[dict(m['questions'][0],source=m['title'],sourceId=m['id']),dict(m['questions'][1],source=m['title'],sourceId=m['id'])]
Path('dist/curriculum.js').write_text('const curriculum = '+json.dumps(DATA,ensure_ascii=False)+';\n',encoding='utf-8')
print('Created 150 modules, 450 focus questions, 300 review questions.')
