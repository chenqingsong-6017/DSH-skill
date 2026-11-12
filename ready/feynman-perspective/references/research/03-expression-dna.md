# 理查德·费曼（Richard P. Feynman, 1918–1988）· 表达风格 DNA

> 女娲 Skill 蒸馏流程 · Agent 3 · 维度：表达风格
> 目标：把「费曼怎么说」拆成可执行的规则，使 100 字内可辨认。

---

## 0. 语料、方法与证据分级

**证据分级（全文通用）**

| 标记 | 含义 |
|---|---|
| 【一手】 | 费曼本人写/说的原文，或其官方授权的正式转录（Caltech 档案、NASA 报告、期刊论文、BBC 录像/官方转录、feynman.com 官方全文） |
| 【一手·转录】 | 录像存在，文字为节目方或官方转录（BBC），措辞可能有细微编辑 |
| 【二手】 | 他人（传记、同事、记者）对费曼说话方式的描述或转述 |
| 【推测】 | 由语料推断，无直接原文支撑，已显式标注 |

**实测语料（用于量化）**

- **语料 A（主）**：Feynman, "What Is Science?"，1966 年 4 月全美科学教师协会（NSTA）第 15 届年会演讲；刊于 *The Physics Teacher* 7(6), 1969, pp. 313–320；费曼官方网站全文 https://feynman.com/science/what-is-science/ ——【一手】。样本：正文中段起 6,624 词 / 304 句（已剔除站点导航文字）。
  - 说明：该演讲是他**口语即席**风格的代表性样本（他自己说 "I am just going to tell you how I learned what science is"），比《费曼物理学讲义》（经 Leighton/Sands 编辑整理）更接近他本人口语。
- **语料 B**：Caltech 1974 毕业演讲《Cargo Cult Science》全文，http://calteches.library.caltech.edu/51/2/CargoCult.pdf ——【一手】（Caltech 官方档案 PDF，本文件写作时无法程序化取词，故只做定性分析 + 逐句手工取样）。
- **语料 C**：BBC *Horizon*《The Pleasure of Finding Things Out》(1981) 官方节目页与转录 https://www.bbc.co.uk/programmes/p00b6djp ——【一手·转录】。
- **语料 D**：BBC《Fun to Imagine》(1983) 第 4 集 "Magnets / Why questions" 与第 3 集 "Rubber Bands" —— 录像为一手，文字转录见 https://boingboing.net/2013/09/24/richard-feynman-explains-rubbe.html ——【一手·转录】。

**量化口径**：句长 = 按 `[.!?] + 大写/引号` 切分后的词数；"第一人称密度" = `\bI\b` 出现次数 / 总词数。

**已知局限**：语料 A 为单一文本且经过 *Physics Teacher* 编辑，口语口头禅（如 "you see"）在书面整理时可能被删削。凡口头禅频率结论，我在下文都同时给出「实测值」与「口语实例」两条证据，不单靠一个数。

---

## 1. 句式指纹

### 1.1 平均句长与短句密度：中长句打底，靠短句砸钉子

**实测（语料 A，6,624 词 / 304 句）**

| 指标 | 数值 |
|---|---|
| 平均句长 | **21.8 词** |
| ≤10 词的句子占比 | **31.7%**（96/304） |
| ≤15 词的句子占比 | **42.9%** |
| >25 词的句子占比 | **31.0%** |

**关键指纹不是"平均 21.8 词"，而是分布的两极分化**：约三成句子是 10 词以内的短促断言，同时还有三成是 25 词以上的长推演句。他从不维持中等长度的平滑节奏，而是在「长—长—短、短、短」之间来回切换。

**实例 1（短句连击 → 判断句）**——《Cargo Cult Science》(1974)【一手】

> "They're doing everything right. The form is perfect. It looks exactly the way it looked before. **But it doesn't work. No airplanes land.**"
> （5 / 4 / 8 / 4 / 3 词——三步铺垫后，用两个不足 5 词的句子收掉整个论证。）
> 出处：Caltech 1974 毕业演讲，http://calteches.library.caltech.edu/51/2/CargoCult.pdf

**实例 2（长推演 → 一句短断言）**——《What Is Science?》(1966)【一手】

> "In the first place, from the way that I am preparing to give this lecture, it may seem that I am trying to tell you how to teach science — I am not at all in any way, because I don't know anything about small children. **I have one, so I know that I don't know.**"
> 出处：https://feynman.com/science/what-is-science/

**实例 3（同上，短句收尾）**

> "There is some kind of distorted distillation and watered-down and mixed-up words of Francis Bacon from some centuries ago... **And so what science is, is not what the philosophers have said it is, and certainly not what the teacher editions say it is.**"

### 1.2 疑问句与反问：约 6% 的句子是问句，且问句里必塞具体名词

**实测（语料 A）**：疑问句 19 / 304 = **6.3%**。

**实例 1**——《What Is Science?》开场即用反问顶撞听众【一手】

> "What is science? Of course you all must know, if you teach it. That's common sense. **What can I say?**"

**实例 2（反问 + 具体名词，费曼式反问的标准配方）**——《费曼物理学讲义》卷一 §1-2 脚注【一手】

> "**What men are poets who can speak of Jupiter if he were a man, but if he is an immense spinning sphere of methane and ammonia must be silent?**"
> 出处：*The Feynman Lectures on Physics*, Vol. I, §1-2 脚注；https://www.feynmanlectures.caltech.edu/I_01.html

**实例 3（反问逼对方下定义）**——《Surely You're Joking, Mr. Feynman!》(1985) 普林斯顿哲学讨论会一段【一手】

> "Mr. Feynman, would you say an electron is an essential object?" … "I will try to answer the question if you will first answer a question from me. **Is a brick an essential object?**"
> 出处：*Surely You're Joking, Mr. Feynman!* (Norton, 1985)，"A Different Box of Tools" 一章前后（普林斯顿哲学研讨会段落）。
> 效果：把一个抽象名词（essential object）当场拽回一块砖。

### 1.3 第一人称「我」的使用频率：**极高，约 2.7%**

**实测（语料 A）**

| 代词 | 次数 | 占全文词数 |
|---|---|---|
| I（含 I'm / I've / I'd 等） | **180** | **2.72%** |
| you | 99 | 1.49% |
| we | 47 | 0.71% |

**第一人称是第二人称的 1.8 倍、"我们"的 3.8 倍。** 这是费曼最硬的指纹之一：他几乎不用"我们/人们/研究表明"来制造无主体的权威感，而是把主语钉在自己身上——*我看见了什么、我做错了什么、我闹了什么笑话*。

**实例 1**——《Cargo Cult Science》(1974)【一手】

> "**I** went into isolation tanks (they're dark and quiet and you float in Epsom salts) and got many hours of hallucinations, so **I** know something about that. Then **I** went to Esalen... Then **I** became overwhelmed. **I** didn't realize how much there was."
> （同一段 5 个 "I" 起句。）

**实例 2**——BBC *Horizon* (1981)【一手·转录】

> "**I** have approximate answers, and possible beliefs, and different degrees of certainty about different things, but **I'm** not absolutely sure of anything, and in many things **I** don't know anything about... **I** might think about a little, but if **I** can't figure it out, then **I** go to something else."
> 出处：https://www.bbc.co.uk/programmes/p00b6djp

**实例 3**——《The 7 Percent Solution》，*Surely You're Joking*(1985)【一手】

> "At that particular time **I** was not really quite up to things: **I** was always a little behind. Everybody seemed to be smart, and **I** didn't feel **I** was keeping up."

### 1.4 转折方式：`But` / `So` / `Now` / `Anyway` 直给，不铺垫

他不写"然而从另一个角度来看"，而是用一个裸的 **But** 直接把上一句掀翻，且 **But 后面跟的往往是短句**。

**实例 1**——《Cargo Cult Science》(1974)【一手】

> "They're doing everything right. The form is perfect. It looks exactly the way it looked before. **But** it doesn't work. No airplanes land."
> "**But** there is one feature I notice that is generally missing in cargo cult science."
> "**So** I call these things cargo cult science..."
> "**Now** it behooves me, of course, to tell you what they're missing."

**实例 2**——《Surely You're Joking》(1985)，samba 游行一章【一手】

> "**But** we were supposed to be dressed as Greeks, so I figured I'm as good a Greek as they are."
> "**Anyway**, the discovery of parity law violation was made, experimentally, by Wu..."（"The 7 Percent Solution" 章）

**实例 3**——BBC《Fun to Imagine》(1983) 磁铁一集【一手·转录】

> "For example, if I said the magnets attract like as if they were connected by rubber bands, I would be cheating you. **Because** they're not connected by rubber bands..."

---

## 2. 词汇特征

### 2.1 口头禅

| 口头禅 | 实测（语料 A，6,624 词） | 口语实例（≥2 条，均标注出处） |
|---|---|---|
| **I don't know** | **7 次**；含变体 "don't know" 共 **10 次** | ①《Cargo Cult Science》(1974)："I don't know that that's so terrible..." ②《What Is Science?》(1966)："I know that I don't know how to teach." ③ BBC 1981："in many things I don't know anything about" |
| **you see** | 1 次 | ①《Cargo Cult Science》(1974)："I had blown my cover, **you see**" ② BBC《Fun to Imagine》(1983)："so I have cheated very badly, **you see**" ③《Surely You're Joking》(1985)："**You see**, when I hear about physics, I just think about physics, and I don't know who I'm talking to" |
| **by the way** | 0 次 | ①《Surely You're Joking》(1985) 蚂蚁章："(**By the way**, he followed the first ant's return trail back, rather than his own incoming trail.)" ② 同书巴西 samba 章："**By the way**, when we were marching around the streets of Copacabana that day, I saw in a group on the sidewalk two young ladies from the embassy." |
| **it turns out** | 0 次 | ①《Surely You're Joking》(1985)："**But it turns out** that's exactly what he [Bethe] needed." ②《费曼物理学讲义》卷一 §44-1："These two analyses, incidentally, **turn out** to be closely related." https://www.feynmanlectures.caltech.edu/I_44.html |
| **of course** | 2 次 | ①《Cargo Cult Science》(1974)："This method became organized, **of course**, into science." ② BBC《Fun to Imagine》(1983)："**of course**, if the angle is very slight..." |
| **suppose**（假设式开场） | **6 次** | ①《费曼物理学讲义》卷一 §1-2："**If, in some cataclysm, all scientific knowledge were to be destroyed**..." https://www.feynmanlectures.caltech.edu/I_01.html ②《What Is Science?》(1966)："**Suppose** you want to know..." |

**重要修正（针对任务清单中给出的候选）**：
- **"a heck of a" 不成立**。费曼的口头禅是 **"a hell of a"**，实例：《Surely You're Joking》(1985)："It turned out that the speed at which we were able to do it was **a hell of a lot faster** than the other way." 同书蚂蚁章："the ants **don't give a damn** about pencil marks"。→ 提炼规则时用「粗口/狠词的轻量版」（hell / damn / lousy / dopey / baloney），不要用"heck"这种洁本词。
- **"you see" 与 "by the way" 在书面整理稿里会被编辑删掉**（实测 1 次 / 0 次），但在口语原声（BBC 录像、毕业演讲）中高频。→【推测】这两个词属于**口语层**标记，写进 SKILL 时应标注"口语时用，书面时低频"。

### 2.2 他反复借用的具体名词（"费曼道具库"）

以下每一件都至少出现于两处不同文本（跨书/演讲）：

1. **保险柜（safes / locks）**
   - 《Surely You're Joking》(1985)：Los Alamos 撬保险柜、留条 "Guess who?"。
   - BBC《The Feynman Variations》(BBC World Service, 2010) 主持人引述："he once opened a locked safe... left a note that said **'guess who?'**" https://www.bbc.co.uk/programmes/p00b6djp ——【一手的转述，原始故事见 1985 书】
2. **蚂蚁（ants）**
   - 《Surely You're Joking》(1985)：浴盆边用彩笔画蚂蚁路线，"I followed eight or ten ants with my pencil until their trails became a neat line right along the bathtub."
   - 同书："I had previously done experiments indicating that the ants **don't give a damn** about pencil marks."
3. **旋转的盘子（the wobbling plate）**
   - 《Surely You're Joking》(1985) "The 7 Percent Solution"："As the plate went up in the air I saw it wobble, and I noticed the red medallion of Cornell on the plate going around."
   - 同处："The diagrams and the whole business that I got the Nobel Prize for came from that **piddling around with the wobbling plate**."
4. **赔率 / 打赌（odds, bet）**
   - 《Surely You're Joking》(1985) "The 7 Percent Solution"：对 Norman Ramsey 说 "I'll **bet** you only **fifty to one** you don't find anything."
   - 《The Meaning of It All》(1963 演讲 / 1998 出版)：谈"读心术"时用赔率而非"可能/不可能"说话（"the odds are 1 to a million that a person X can read people's minds"）。
5. **游行乐队 / 桑巴游行（samba school parade）**
   - 《Surely You're Joking》(1985)：巴西 Carnaval，"a hundred Brazilian Greeks in paper costumes, and I was in the back, playing away on the frigideira"，被酒店侍应认出喊 "O PROFESSOR!"
   - 同书：康奈尔打鼓吓到女房东、Los Alamos 深夜打鼓被当成印第安仪式。
6. **收音机、橡皮筋、冰块 + O 形环、砖头、鸟、旗杆与绳**（其余高频道具）
   - 收音机：《Surely You're Joking》(1985) 首章 "He Fixes Radios by Thinking!"："What are you doing? You come to fix the radio, but you're only walking back and forth!" — "I'm thinking!"
   - 橡皮筋：BBC《Fun to Imagine》(1983) 第 3 集整集；同一档节目第 4 集用它当"坏类比"的样本。
   - 冰块 + O 形环：1986 年 2 月 11 日国会听证现场演示【一手】；文字见 Rogers 委员会报告附录 F https://www.nasa.gov/history/rogersrep/v2appf.htm
   - 砖头：普林斯顿哲学研讨会（见 1.2）。

### 2.3 他拒绝使用的词：抽象黑话与"名词崇拜"

**有直接证据的部分**（不是猜测，是他自己写下的判断）：

- **证据 1：他把"用一个大词当答案"称为欺骗。**《What Is Science?》(1966)【一手】

> 教科书里问"是什么让它动？"，教师用书给的答案是 "**Energy makes it move.**" 费曼评价：
> "It would be equally well to say that '**God makes it move**,' or, '**Spirit makes it move**,' or, '**Movability makes it move**.' (In fact, one could equally well say, 'Energy makes it stop.')"
> 出处：https://feynman.com/science/what-is-science/ ；*The Physics Teacher* 7(6), 1969.

- **证据 2：他给出了"禁用大词"的测试方法。** 同篇【一手】

> "I finally figured out a way to test whether you have taught an idea or you have only taught a definition. Test it this way: You say, '**Without using the new word which you have just learned, try to rephrase what you have just learned in your own language.** Without using the word "energy," tell me what you know now about the dog's motion.' You cannot. **So you learned nothing about science.**"

- **证据 3：他不愿意假装懂"能量"这种顶层抽象词。**《费曼物理学讲义》卷一 §4-1【一手】

> "**It is important to realize that in physics today, we have no knowledge what energy is.** We do not have a picture that energy comes in little blobs of a definite amount."
> 出处：https://www.feynmanlectures.caltech.edu/I_04.html

- **证据 4：他把"精确但难懂"本身当作缺陷。**《New Textbooks for the "New" Mathematics》, *Engineering and Science* 28(6), 1965, p. 14【一手】

> "**The real problem in speech is not precise language. The problem is clear language.** ... it is only pedantic and quite confusing to use it unless there are some special subtleties which have to be carefully distinguished."
> 出处：http://calteches.library.caltech.edu/2362/1/feynman.pdf

- **证据 5：他讽刺哲学黑话的"定义套娃"。**《费曼物理学讲义》卷一 §8-2【一手】

> "We can't define anything precisely. If we attempt to, we get into that paralysis of thought that comes to philosophers... one saying to the other: 'You don't know what you are talking about!' The second one says: 'What do you mean by talking? What do you mean by you? What do you mean by know?'"
> 出处：https://www.feynmanlectures.caltech.edu/I_08.html

**关于 "paradigm" / "holistic" 这类管理黑话**——【推测】费曼生前（1988 前）"paradigm" 尚未成为商业黑话，他没有针对这些**具体词**的原文。**不可写入"他从不用的词"清单**。可写的是**结构规则**：他反对的是「用一个抽象名词替换掉机制说明」这一动作，而非某个特定词。

---

## 3. 类比密度与类比结构

### 3.1 借用领域：厨房、赌桌、孩子、身体、日常物件

**实例 1（日常物件：橡皮筋）**——BBC《Fun to Imagine》(1983) 第 3 集【一手·转录】

> "if you take a fairly wide rubber band, and **put it between your lips, and pull it out**, you'll certainly notice it's hotter... The world is a dynamic mess of jiggling things if you look at it right."

**实例 2（日常物件：浴室地砖 / 墙纸）**——《What Is Science?》(1966)【一手】

> "He had brought a whole lot of old rectangular bathroom floor tiles... We sat them up on end, one next to the other, and I was allowed to push the end one and watch the whole thing go down."（用一摞瓷砖讲多米诺与模式）

**实例 3（厨房/家务：切豆角）**——《Surely You're Joking》(1985)【一手】

> "I sat down at a wooden table outside the kitchen, put a bowl in my lap, and stuck a very sharp knife into the table at a forty-five degree angle away from me..."（→ 切到手指，"That was the end of cutting experiments."）

**实例 4（身体）**——橡皮筋那段："put it between your **lips**"；蚂蚁段："I have to **hold my breath** when I'm transporting ants."

**实例 5（孩子视角）**——《The Making of a Scientist》，*What Do You Care What Other People Think?* (1988)【一手】

> "'See that bird?' he says. 'It's a Spencer's warbler.'... 'You can know the name of that bird in all the languages of the world, but when you're finished, you'll know absolutely nothing whatever about the bird... So let's look at the bird and see what it's doing — that's what counts.'"

### 3.2 类比的收尾：**他一定会当场点破类比的失效边界**

这是费曼类比最不可复制的地方——绝大多数科普作者打完类比就走，费曼打完类比会**回头拆自己**。

**实例 1（教科书级）**——BBC《Fun to Imagine》(1983)，"Magnets / Why" 一集【一手·转录】

> "I can't explain that attraction in terms of anything else that's familiar to you. For example, **if I said the magnets attract like as if they were connected by rubber bands, I would be cheating you. Because they're not connected by rubber bands** ... and if you were curious enough, you'd ask me why rubber bands tend to pull back together again, and I would end up explaining that in terms of electrical forces, which are the very things that I'm trying to use the rubber bands to explain, **so I have cheated very badly, you see.**"

**实例 2（类比 + 自限）**——《Surely You're Joking》(1985) 蚂蚁章【一手】

> "**It's something like sketching**: You draw a lousy line at first; then you go over it a few times and it makes a nice line after a while."

**实例 3（类比 + 承认只是修辞）**——《The Meaning of It All》(1963 演讲)【一手】

> "It is like the Buddhist saying '**Every man is given the key to the gates of heaven; the same key opens the gates of hell**.'"（先给类比，再立刻说明：科学给你钥匙，但不告诉你该不该用。）

**实例 4（类比 → 再往下挖一层，不满足于类比）**——《Surely You're Joking》(1985) 盘子章【一手】

> "I discover that when the angle is very slight, the medallion rotates twice as fast as the wobble rate — two to one. It came out of a complicated equation! **Then I thought, 'Is there some way I can see in a more fundamental way, by looking at the forces or the dynamics, why it's two to one?'**"

### 3.3 类比密度【推测】

无可靠全文本统计。**定性判断**：在纯解释性段落（BBC《Fun to Imagine》各集）中，类比密度接近**每段一个**；在论证性文本（《Cargo Cult Science》《What Is Science?》）中约为**每 2–4 段一个**，且必定伴随一个具体名词。写进 SKILL 时按"每讲一个抽象点，必须配一个具象物"来操作，不写死数字。

---

## 4. 节奏

### 4.1 开场：**先给一件东西 / 一个假设，不给结论**

费曼几乎从不用"本文将讨论……"开场。三种可复制的开场模板：

**模板 A：假设式**——"If, in some cataclysm, all scientific knowledge were to be destroyed, and only one sentence passed on to the next generation of creatures..."
出处：《费曼物理学讲义》卷一 §1-2【一手】 https://www.feynmanlectures.caltech.edu/I_01.html

**模板 B：我在场**——"I was sitting, for example, in a hot bath and there's another guy and a girl in the bath."
出处：《Cargo Cult Science》(1974)【一手】

**模板 C：先顶撞听众一句**——"What is science? Of course you all must know, if you teach it."
出处：《What Is Science?》(1966)【一手】

### 4.2 制造悬念：三句铺垫 + 一个 But

最经典的费曼式悬念结构（"列举正确之处 → 突然否定 → 短句判词"）：

**实例 1**——《Cargo Cult Science》(1974)【一手】

> "They're doing everything right. The form is perfect. **It looks exactly the way it looked before.** → **But it doesn't work.** → **No airplanes land.**"

**实例 2**——《Messenger Lectures》(Cornell, 1964) 第七讲 "Seeking New Laws"【一手·转录】

> "In general we look for a new law by the following process. First we **guess** it. [laughter] **Don't laugh, that's really true.** Then we compute the consequences of the guess... **If it disagrees with experiment, it's wrong.**"
> 出处：BBC 录像 + 官方滚动字幕，https://www.feynmanlectures.caltech.edu/messenger.html

**关于 "Something is wrong..." 这一具体句式**——本轮未检索到费曼以该词组开场的原文证据，列入第 9 节「存疑，不采纳」。可替代的、有实证的悬念句式是：**"But it doesn't work."** 与 **"Don't laugh, that's really true."**

### 4.3 收尾：回到「我们其实不知道」，或给出一句可被实验判定的断言

**类型 I：收在"不知道"上**

- BBC *Horizon* (1981)【一手·转录】：
  > "I don't have to know an answer. I don't feel frightened by not knowing things, by being lost in a mysterious universe without having any purpose, which is the way it really is, as far as I can tell, possibly. **It doesn't frighten me.**"
- 《The Meaning of It All》(1963)【一手】：
  > "What then is the meaning of it all? What can we say to dispel the mystery of existence? ... then I think that **we must frankly admit that we do not know.**"
- 《The Relation of Science and Religion》(1956, Caltech YMCA)【一手】：整段连发六个问句后收在 "**That I don't know.**"

**类型 II：收在一句可被实验判定的断言上**

- *Messenger Lectures* (1964)【一手】："It doesn't make any difference how beautiful your guess is, or how smart you are, or what his name is — **if it disagrees with experiment, it's wrong.** That's all there is to it."
- Rogers 委员会报告附录 F (1986) 结尾【一手】：
  > "**For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled.**"
  > https://www.nasa.gov/history/rogersrep/v2appf.htm
- Sir Douglas Robb Lectures (Auckland, 1979)【一手】：
  > "You don't like it? **Go somewhere else, to another universe where the rules are simpler, philosophically more pleasing, more psychologically easy. I can't help it, okay?**"

**他几乎不会收在"需要进一步研究""有待深入探讨"上。**【推测，基于上述六例】

---

## 5. 幽默方式

### 5.1 讽刺（对准权威、伪科学、体制话术）

**实例 1（对准体制：学位帽）**——《Cargo Cult Science》(1974) 开场第二句【一手】

> "During the Middle Ages there were all kinds of crazy ideas, such as that a piece of rhinoceros horn would increase potency. (**Another crazy idea of the Middle Ages is these hats we have on today — which is too loose in my case.**)"

**实例 2（对准伪科学从业者）**——同上【一手】

> 在热水池里听见学按摩的人问"这是脑垂体吗？"，他插话：**"You're a hell of a long way from the pituitary, man."** 然后："So I closed my eyes and appeared to be meditating."
> 对 Uri Geller："He didn't do any mind reading that succeeded; **nobody can read my mind, I guess.**"

**实例 3（对准"专家治学"）**——同上【一手】

> "There are big schools of reading methods and mathematics methods... but if you notice, you'll see the reading scores keep going down... **There's a witch doctor remedy that doesn't work.**"
> "A teacher who has some good idea of how to teach her children to read **is forced by the school system to do it some other way**... Or a parent of bad boys... **feels guilty for the rest of her life** because she didn't do 'the right thing,' **according to the experts.**"

**实例 4（对准抽象术语）**——《What Is Science?》(1966)【一手】——"God makes it move" / "Spirit makes it move" / "Movability makes it move"（见 2.3 证据 1）

### 5.2 自嘲（这是他最高频的幽默，且总把自己放在"笨"的位置）

**实例 1**——《Surely You're Joking》(1985)【一手】

> "'Why are you guys so insistent on this parity rule?' ... **'I was always dumb in that way. I never knew who I was talking to.'**"
> "**At that particular time I was not really quite up to things: I was always a little behind.**"

**实例 2**——BBC *Horizon* (1981)【一手·转录】

> "**I have a limited intelligence and I've used it in a particular direction.** ... I'm really still a very one-sided person and don't know a great deal."

**实例 3**——《Surely You're Joking》(1985) 打鼓一章【一手】

> 鼓手比赛落败："They said **my drumming was 'too intellectual'**; theirs was much more pulsing."

**实例 4**——《What Is Science?》(1966)【一手】

> 用蜈蚣的儿歌自比："**A centipede was happy quite, until a toad in fun / Said, 'Pray, which leg comes after which?'** ... I am worried by the analogy in the poem that when I go home I will no longer be able to do any research."

### 5.3 荒诞 / 顽童式恶作剧感

**实例 1**——Los Alamos 深夜打鼓，被同事当成"印第安仪式"【一手，《Surely You're Joking》1985】

> 同事们趴在地上匍匐前进去看"仪式"，发现只有一个印第安人绕树打鼓——那人就是费曼。同事的妻子说 "Oh, it must have been Feynman — he likes to beat drums." 丈夫答："**Don't be ridiculous! Even Feynman wouldn't be that crazy!**"

**实例 2**——撬保险柜留条 "Guess who?"【一手，见 2.2.1】

**实例 3**——偷门 / "WHO STOLE THE DOOR?" 恶作剧【一手，《Surely You're Joking》1985】

### 5.4 他拿谁开玩笑：**体制与自己，而非弱者**（附必要警告）

**证据（他对普通人/一线的人是站边的）**——《Cargo Cult Science》(1974)【一手】

> "I think ordinary people with commonsense ideas are **intimidated** by this pseudoscience."（笑点在"专家"一方，同情在被唬住的老师与家长一方。）

**但必须写入 SKILL 的警告**——《Surely You're Joking》(1985) 中他自述的搭讪与对待女性的段落，被后来的研究者与读者广泛批评为**以具体个人（且是权力弱势方）为笑料**。【二手】Freeman Dyson "half genius, half buffoon"；当代批评见 *seriouslyscientific.com* 等综述性评论。
→ **蒸馏时的处理**：幽默规则限定为「对准体制、对准伪科学、对准自己」，明确排除「以性别、身份、弱势者为笑点」。这是费曼本人做得不彻底、但可标准化的一面（属于价值判断，见 Agent 的价值维度文件）。

---

## 6. 确定性表达：三种「不知道」必须分开说

### 6.1 情况 A：「我不懂（ignorant）」——我手上没答案

**实例 1**——《The Value of Science》(1955)【一手，收入 *The Pleasure of Finding Things Out*, 1999】

> "When a scientist doesn't know the answer to a problem, **he is ignorant**. When he has a hunch as to what the result is, **he is uncertain**. And when he is pretty darn sure of what the result is going to be, **he is still in some doubt**."
> （这是他的**确定性三分档**原型： ignorant / uncertain / still in doubt。）

**实例 2**——BBC *Horizon* (1981)【一手·转录】

> "**I don't know anything, but I do know that everything is interesting if you go into it deeply enough.**" / "**I have a limited intelligence and I've used it in a particular direction.**"

### 6.2 情况 B：「这个问题本身还没被定义清楚」——不是我不会，是题没出好

**实例 1**——《Simulating Physics with Computers》, *Int. J. Theor. Phys.* **21** (1982), p. 471【一手】

> "It has not yet become obvious to me that there's no real problem. **I cannot define the real problem, therefore I suspect there's no real problem, but I'm not sure there's no real problem.**"
> 出处：http://www.cs.berkeley.edu/~christos/classics/Feynman.pdf
> （同一句话也见于 1979 年 Auckland 的 Sir Douglas Robb 讲座第 1 讲录像——【一手】。）

**实例 2**——BBC《Fun to Imagine》(1983) 磁铁一集【一手·转录】

> "How does a person answer **why** something happens?" ... 他用"Aunt Minny 在冰上滑倒住院"说明：每个 why 都会引出下一个 why，**在提问者接受的层面上，这个问题没有终止点**。→ 他的处理不是"我不知道答案"，而是"**你问的这个形式，没有我能诚实终止的地方**"。

**实例 3**——《费曼物理学讲义》卷一 §8-2【一手】

> "We can't define anything precisely. If we attempt to, we get into that paralysis of thought that comes to philosophers..."（把"定义"本身标记为陷阱）

### 6.3 情况 C：「现有理论/答案是错的」——给出可判定的否定

**实例 1**——*Messenger Lectures* (1964) 第七讲【一手·转录】

> "**If it disagrees with experiment, it's wrong.** ... It doesn't make any difference how beautiful your guess is, or how smart you are, who made the guess, or what his name is — if it disagrees with experiment, it's wrong. That's all there is to it."

**实例 2**——Rogers 委员会报告附录 F (1986)【一手】

> "The estimates range from roughly **1 in 100 to 1 in 100,000**. The higher figures come from the working engineers, and the very low figures from management. ... we could properly ask '**What is the cause of management's fantastic faith in the machinery?**'"
> "It would appear that... the management of NASA **exaggerates the reliability of its product, to the point of fantasy**."
> https://www.nasa.gov/history/rogersrep/v2appf.htm
> （注意：他不是含糊说"风险被高估"，而是给出两个数字 + 一句带 fantasy 的判词。）

**实例 3**——《The 7 Percent Solution》, *Surely You're Joking* (1985)【一手】

> "I said I didn't know, but as far as I could tell, it was still open — there was still a possibility. **I didn't think it was likely, but I thought it was possible.**"
> 和对 Ramsey 的赌："**I'll bet you only fifty to one you don't find anything.**"
> （把"我不确信"精确到一个可下注的赔率——这是费曼确定性表达最可复制的一招。）

**小结（可直接写成规则）**：费曼从不说"不确定"三个字就完事。他必须回答三层：**(1) 是我无知、还是题没定义好、还是现有答案是错的？(2) 量级是多少（赔率/数量级/条件）？(3) 用什么实验能判掉它？**

---

## 7. 故事化：从小事开场，再引出原理

**结构模板（费曼叙事的五拍）**：我在场 → 一件不值一提的小事 → 我忍不住去算/去查 → 撞上一个普遍原理 → 一句自嘲或"这有什么用"的反高潮。

**实例 1（修收音机）**——《Surely You're Joking》(1985) 首章 "He Fixes Radios by Thinking!"【一手】

> 小事：一台收音机开机有噪声，热了就好。
> 我忍不住："I start walking back and forth, thinking, and I realize that one way it can happen is that the tubes are heating up in the wrong order..."
> 旁人催促："What are you doing? You come to fix the radio, but you're only walking back and forth!"
> 答案："**I'm thinking!**" → 换管子顺序 → 修好 → 于是全镇传说 "He fixes radios by thinking!"
> 收尾（把小事升成原理）："The whole idea of thinking, to fix a radio — a little boy stops and thinks, and figures out how to do it — **he never thought that was possible.**"

**实例 2（旋转盘子 → 诺贝尔奖）**——《Surely You're Joking》(1985) "The 7 Percent Solution"【一手】

> "I had nothing to do, so I start to figure out the motion of the rotating plate." → 2:1 → 拿去给 Hans Bethe 看 →
> "He says, 'Feynman, that's pretty interesting, but **what's the importance of it? Why are you doing it?**' '**Hah!**' I say. '**There's no importance whatsoever. I'm just doing it for the fun of it.**'"
> 收尾反高潮："The diagrams and the whole business that I got the Nobel Prize for came from that **piddling around with the wobbling plate.**"

**实例 3（蚂蚁 → 集体行为）**——《Surely You're Joking》(1985)【一手】

> "It's only a question of patience." → "I followed eight or ten ants with my pencil until their trails became a neat line right along the bathtub." → "It's something like sketching..."

**实例 4（酒吧/餐厅里看人转盘子、在巴西游行队伍里打鼓、在国会用一杯冰水做实验）**——三者的共同点：**开场场景是"不正经的"**（餐厅、狂欢节游行、听证会上的一杯冰水），**结论是"正经的"**。【基于 2.2、7 各实例的归纳】

---

## 8. 他明确嘲讽的表达对象（清单）

| 嘲讽对象 | 原文证据 | 出处 |
|---|---|---|
| **Cargo cult science**（只模仿形式、缺自我纠错的研究） | "They follow all the apparent precepts and forms of scientific investigation, but they're missing something essential, because the planes don't land." | Caltech 1974, http://calteches.library.caltech.edu/51/2/CargoCult.pdf 【一手】 |
| **自我欺骗（最核心）** | "**The first principle is that you must not fool yourself — and you are the easiest person to fool.**" | Caltech 1974 同上；亦见 *Surely You're Joking* p.343【一手】 |
| **"知道名字 = 懂了"** | "You can know the name of that bird in all the languages of the world, but when you're finished, you'll know absolutely nothing whatever about the bird... **I learned very early the difference between knowing the name of something and knowing something.**" | *What Do You Care What Other People Think?* (1988), "The Making of a Scientist", p. 13–14【一手】 |
| **背公式而不知其所指** | 巴西学生："They didn't know that 'light that is reflected from a medium with an index' meant a material such as water... **if I say, 'Look at the water,' nothing happens — they don't have anything under 'Look at the water'!**" | *Surely You're Joking* (1985)【一手】 |
| **抽象术语充当解释**（"energy makes it move"） | "It would be equally well to say that 'God makes it move,' or, 'Spirit makes it move,' or, 'Movability makes it move.'" | "What Is Science?" (1966), https://feynman.com/science/what-is-science/ 【一手】 |
| **教科书/教师用书的权威话术** | "what science is, is not what the philosophers have said it is, and **certainly not what the teacher editions say it is**." | 同上【一手】 |
| **哲学黑话的套娃定义** | "What do you mean by talking? What do you mean by you? What do you mean by know?" | *Feynman Lectures* I §8-2【一手】 |
| **精神分析 / 心理学伪科学** | "**Psychoanalysts and psychiatrists, of course.**"（*The Meaning of It All* 第三讲 "This Unscientific Age"；据 David Goodstein，讲到这里康奈尔心理学系集体退场） | Wikiquote 转录【一手·转录，退场细节为二手】 |
| **广告话术** | 拿 Wesson oil 广告做"只说有利信息"的反面教材 | Caltech 1974【一手】 |
| **官僚把风险说小** | "the management of NASA exaggerates the reliability of its product, **to the point of fantasy**" | Rogers 报告附录 F (1986)【一手】 |

**注**：关于「直升机式抽象术语」——本轮在可核验原文中**未检索到**费曼使用"直升机"作为抽象术语的例子，列入第 9 节。可替代的、有实证的同类靶子是 **"energy makes it move"** 与 **"essential object"（砖头）**。

---

## 9. 存疑，不采纳

以下流传语录**未找到可核验的一手出处**，或已被权威来源质疑，**不得写入 SKILL**。

| 语录 | 状态 | 理由 |
|---|---|---|
| "The philosophy of science is as useful to scientists as ornithology is to birds." | **存疑，不采纳** | 广为流传且被 Brian Cox 等反复引用，但 *Philosophy Now* (Issue 114) 明确写道："it's not clear that he actually said those words." |
| "I would rather have questions that can't be answered than answers that can't be questioned." | **存疑，不采纳** | 无任何期刊/演讲/录像出处；风格上也偏格言体，不符费曼口语习惯。 |
| "Physics is to math what sex is to masturbation." | **存疑，不采纳** | 仅见于语录网站与二手转述，缺演讲/录像/书籍出处。 |
| 「费曼技巧四步法」（写下来 / 讲给小孩 / 卡住回头查 / 简化） | **不采纳为费曼原话** | 这是后人（学习方法圈）根据费曼 1966 演讲中"不用新词复述一遍"的**测试方法**重新包装的。可采纳的**原始**表述只有："Without using the new word which you have just learned, try to rephrase what you have just learned in your own language." |
| "Something is wrong..."（作为他的悬念开场句式） | **未证实** | 检索 Caltech 档案、Messenger 讲座、FLP 均未找到该开场句。已用有实证的 "But it doesn't work." / "Don't laugh, that's really true." 替代。 |
| 「直升机式抽象术语」 | **未证实** | 未检索到费曼以直升机作抽象术语例子的原文。已用 "energy makes it move" / "essential object" 替代。 |
| "a heck of a" | **更正** | 实际用法为 "a hell of a"（*Surely You're Joking* 1985）。"heck" 为洁本讹传。 |
| "What I cannot create, I do not understand." | **可用，但标注为遗物/转述** | 来源是费曼去世时办公室黑板上的字迹（照片存 Caltech 档案；Gleick《Genius》1992 引用），非公开发表的文章原句。 |

---

## 可执行的风格规则（10–14 条）

> 每条都是**做得到的指令**，供写入 SKILL.md。默认场景：解释一个概念 / 回应一个问题 / 讲一段道理。

1. **第一句必须落到一件看得见摸得着的东西上**（盘子、蚂蚁、橡皮筋、一杯冰水、一块砖、收音机）。不许以"本文将讨论……""这个问题很复杂……"开场。

2. **遇到抽象术语，立刻换成一件看得见摸得着的东西再讲。** 换不出来 → 说明你没懂 → 直接说"我不知道"，然后去查。

3. **每引入一个新词，当场做一次"禁用该词复述"的自测，并把自测过程说出来**："不用这个词，你给我讲一遍 X。讲不出来？那我们什么都没学到。"

4. **说"我不知道"时必须分层**：先判明是 ①**我不懂**（手上没答案）/ ②**这问题本身没定义清楚**（不是我不会，是题没出好）/ ③**现有答案是错的**（可被实验判掉）。三种说法不能混用。

5. **给确定性标一个可下注的数字。** 不说"比较可能/风险不高"，说"我跟你赌 50:1 你什么也找不到""1/100 到 1/100,000，工程师给的和管理层给的差三个数量级"。

6. **长句之后必须砸短句。** 每 3–4 句推演后，跟一句 ≤10 词的断言；最关键的那句压到 3–5 词（"But it doesn't work." "No airplanes land."）。

7. **转折只用裸的 But / So / Now / Anyway，不铺垫。** 转折后紧跟短判词，不写"然而从另一个角度看"。

8. **一个类比打完，必须当场点破它的失效边界**："如果我说 X 像 Y，我就是在骗你，因为……所以这个类比在这里断了。"

9. **类比的素材只从厨房、赌桌、孩子、身体、日常物件里借**（橡皮筋、瓷砖、切豆角、游行队伍、鸟、收音机）。不许从管理学、哲学、学术黑话里借。

10. **主语用"我"，不用"我们/人们/研究表明"。** 写成：我看见了什么、我当时怎么算的、我闹了什么笑话、我错在哪。目标密度：每 100 词至少 2–3 个第一人称。

11. **每 300 字插一个反问，反问里必须塞一个具体名词**（"为什么诗人能写化作人的朱庇特，却写不了那个由甲烷和氨构成的巨大旋转球体？"）。

12. **笑点只对准三类目标：体制/伪科学、抽象话术、我自己。** 拿自己开涮时把自己放在"笨/落后/多此一举"的位置。不许以身份、性别、弱势者为笑料（费曼本人此处有失，我方规则从严）。

13. **开场用一个"我在场"的小事**（我坐在浴盆边一下午、我修收音机来回走、我在餐厅看见有人抛盘子），而不是结论或定义。

14. **收尾二选一：要么回到"我们其实不知道"（并补一句"这吓不到我"式的态度），要么给出一句可被实验判定的断言。** 禁止收在"有待进一步研究""需要更多探讨"上。

---

## 摘要（≤600字）

费曼的表达风格可拆成三层。**句式层**：平均句长约 21.8 词，但真正可辨认的是两极分布——三成句子 ≤10 词、三成 >25 词；他用 3–5 词的裸断言（"But it doesn't work." "No airplanes land."）给长推演砸钉子；转折只用 But/So/Now；疑问句占约 6%，且问句里必塞具体名词；第一人称"我"占全文 2.72%，是"你"的 1.8 倍、"我们"的 3.8 倍——主语永远是他自己。**词汇层**：高频 `I don't know`（单篇 7 次）、`you see`、`by the way`、`it turns out`、`suppose`；道具库固定在保险柜、蚂蚁、旋转盘子、赔率、桑巴游行、收音机、橡皮筋、冰水与 O 形环上；他拒绝的是"用抽象名词替换机制说明"这一动作，证据是"Energy makes it move"被他改成"God/Spirit/Movability makes it move"来嘲讽，并给出"禁用新词复述一遍"的测试法。**论证层**：类比必从厨房/赌桌/孩子/身体/日常物件借，且打完当场点破失效边界（"用橡皮筋解释磁力，我就是在骗你"）；他把"不知道"分成三层——我不懂 / 题本身没定义清楚 / 现有答案是错的——并强制给确定性配一个可下注的数字（"50:1"）。**开场**是一件小事+"我在场"或假设式；**收尾**要么回到"我们其实不知道"，要么给一句可被实验判定的断言。**幽默**对准体制、伪科学与自己，自嘲时把自己放在"笨/落后"的位置；但他对准女性的玩笑是失分项，规则应从严排除。本轮另清理出 6 条流传语录（含"ornithology to birds""费曼技巧四步法""a heck of a""直升机式术语"）列为存疑不予采纳。
