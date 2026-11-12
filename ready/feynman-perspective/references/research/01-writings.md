# 维度 01：著作与系统性长文 — Richard Feynman (1918–1988)

> 调研日期：2026-10-12（Agent 1）
> 任务：提取他**反复表达、跨领域复现**的思维方式（HOW he thinks），供后续提炼心智模型。
> 全文用中文书写；专有名词与英文原文引语保留英文。

---

## 0. 方法与可信度约定

### 三类归属（每条信息必标）
- **【他说过】**＝他本人写的/说的原文（书、讲义、演讲稿、书信、论文、可核验的录音转录）。
- **【别人说他】**＝同事、传记作者、记者的转述与评价（Gleick / Goodstein / Sands / Bethe / Gell-Mann / Preskill 等）。
- **【我推断】**＝我从一手材料交叉比对得出的结论，**显式标注「推测」**，不与前两类混写。

### 可信度三级
- **【一手】**：他本人的文字/声音/手迹，或 Caltech / Nobel / APS / Physics Today 等权威机构的原始存档（含扫描件、官方转录）。
- **【二手】**：带卷/章/页码的引语索引（如 Wikiquote）、权威传记、权威媒体报道、同行回忆。
- **【推测】**：我的归纳，必须写明推理链。

### 信息源黑名单遵守情况
已排除知乎、微信公众号、百度百科/百度知道。**未使用**任何中文百科站（含 baike.baidu.com、baike.com「快懂百科」）——调研中出现过但已主动弃用。
注：`www.feynmanlectures.caltech.edu` 对本次环境的 curl 请求返回 Cloudflare 403，无法直接抓正文；该站的引语通过「带卷-章-页码的二手索引 + feynmanlectures.caltech.edu 官方子页面（可访问）+ Caltech 档案扫描件」三角核验后使用，凡无法三角核验的一律降级为【二手】或移入「存疑」。

---

## 1. 反复出现 ≥3 次的核心论点（真信念）

### 论点 A：理解 = 能重建，不是能记住 / 能叫出名字
**出现次数：6 次以上，横跨 1940s–1988，跨越物理学、教学法、学习观、艺术。**

1. 【他说过】【一手】1988-02 去世时 Caltech 办公室黑板上的两行字：
   > "What I cannot create, I do not understand." / "Know how to solve every problem that has been solved."
   > 出处：Caltech Archives 照片 `https://digital.archives.caltech.edu/collections/Images/1.10-29/`（原 `archives.caltech.edu/pictures/1.10-29.jpg`）
2. 【他说过】【一手】《Feynman Lectures on Computation》Ch.1 "Introduction to Computers"（课程 1983–86，书 1996）：
   > "It's the way I study — to understand something by trying to work it out or, in other words, to understand something by creating it. Not creating it one hundred percent, of course; but taking a hint as to which direction to go but not remembering the details. These you work out for yourself."
   > 同段还有："When I start straight off to read someone else's solution I find it boring and uninteresting, with no way of putting the whole picture together."
   > 出处：`https://icourse.club/uploads/files/cdf0a91886c41581ea984e5ca0aacd57627cc604.pdf`（转录副本，原文 CRC Press / Taylor & Francis）
3. 【他说过】【一手】同一本书的 Preface：
   > "imagine that you are explaining your ideas to your former smart, but ignorant, self, at the beginning of your studies!"
4. 【他说过】【一手】《What Do You Care What Other People Think?》(1988)，"The Making of a Scientist," p.14：
   > "You can know the name of that bird in all the languages of the world, but when you're finished, you'll know absolutely nothing whatever about the bird. … I learned very early the difference between knowing the name of something and knowing something."
   > 同一故事他至少讲过 3 个版本：1966 NSTA 演讲 "What is Science?"；1981 BBC Horizon 访谈（收于 Sykes《No Ordinary Genius》p.27）；1988 上书 p.14。
5. 【他说过】【一手】《Surely You're Joking, Mr. Feynman!》(1985) Part 1, "Who Stole the Door?", p.36-37：
   > "I don't know what's the matter with people: they don't learn by understanding; they learn by some other way — by rote or something. Their knowledge is so fragile!"
6. 【他说过】【一手】1965-11-30 致 J. M. Szabados 信（收于《Perfectly Reasonable Deviations from the Beaten Track》p.206）：
   > "study hard what interests you the most in the most undisciplined, irreverent and original manner possible."
7. 【别人说他】【二手】David Goodstein 回忆：Feynman 主动提出就某个量子统计结果做一次「大一新生水平」的讲座，几天后回来说做不到，于是判定"we really don't understand it"。出处：Goodstein, "Richard P. Feynman, Teacher," *Physics Today* 42(2) (1989-02) p.70-75；另见 *Physics Today* (2017-03) p.11 转述。

**【我推断｜推测】** 这个论点是他全部思维方式里最硬的一条：它不是「学习技巧」，而是**理解的定义本身**。他把"能否从零重建"当作真/假理解的可操作判据——黑板那句话、大一新生测试、Feynman Lectures on Computation 的自述是同一条规则的三个不同投影。后续心智模型建议把它放在第一位。

---

### 论点 B：实验/观察是唯一裁判；猜→推→比对是科学的全部
**出现次数：5 次以上。**

1. 【他说过】【一手】*The Feynman Lectures on Physics*, Vol. I, lecture 1, §1-1, p.1-1：
   > "The test of all knowledge is experiment. Experiment is the sole judge of scientific 'truth'."
2. 【他说过】【一手】*The Character of Physical Law* (1965), ch.7 "Seeking New Laws," p.156（书本编辑版）；口语原版见同章视频转录：
   > "In general, we look for a new law by the following process: First we guess it. Then we — now don't laugh, that's really true. Then we compute the consequences of the guess… And then we compare the computation results to nature… If it disagrees with experiment, it's wrong. In that simple statement is the key to science. It doesn't make any difference how beautiful your guess is, it doesn't make any difference how smart you are, who made the guess, or what his name is. If it disagrees with experiment, it's wrong. That's all there is to it."
   > 视频：`https://www.youtube.com/watch?v=-2NnquxdWFk&t=16m46s`（Cornell Messenger Lectures 官方录音）
3. 【他说过】【一手】*QED: The Strange Theory of Light and Matter* (1985) p.149-150：同一"guess—compute consequences—compare with experiment"公式的再述。
4. 【他说过】【一手】*The Meaning of It All* (1999；1963-04 华盛顿大学演讲) lecture I "The Uncertainty of Science"：
   > "The exception tests the rule. Or, put another way, 'The exception proves that the rule is wrong.' That is the principle of science. If there is an exception to any rule, and if it can be proved by observation, that rule is wrong."
5. 【他说过】【一手】*The Character of Physical Law* ch.7, p.165-166：
   > "It is not unscientific to make a guess, although many people who are not in science think it is. … It is scientific only to say what is more likely and what less likely, and not to be proving all the time the possible and impossible."
6. 【他说过】【一手】*The Character of Physical Law* ch.7, p.171：
   > "You can recognize truth by its beauty and simplicity. … the truth always turns out to be simpler than you thought."

**矛盾（记录，不调和）**：(2)/(4) 说实验是唯一裁判，(6) 却说"你能靠美和简洁认出真理"，并说"远在你检查完所有后果之前就知道自己对了"。他没解释这两条如何统一。见 §5-C。

---

### 论点 C：不许骗自己；「向后弯腰」式的超常诚实
**出现次数：4 次以上，横跨演讲、讲义、致公众写作。**

1. 【他说过】【一手】1974 Caltech 毕业演讲 "Cargo Cult Science"（Caltech 档案馆原件）：
   > "The first principle is that you must not fool yourself — and you are the easiest person to fool. So you have to be very careful about that. After you've not fooled yourself, it's easy not to fool other scientists. You just have to be honest in a conventional way after that."
   > 出处：`http://calteches.library.caltech.edu/51/2/CargoCult.htm`（及 PDF `.../51/2/CargoCult.pdf`）；另收于《Surely You're Joking》p.343
2. 【他说过】【一手】同演讲，"leaning over backwards" 段（这是他对"科学诚信"给出的**完整操作定义**）：
   > "It's a kind of scientific integrity, a principle of scientific thought that corresponds to a kind of utter honesty — a kind of leaning over backwards. For example, if you're doing an experiment, you should report everything that you think might make it invalid — not only what you think is right about it: other causes that could possibly explain your results; and things you thought of that you've eliminated by some other experiment, and how they worked… Details that could throw doubt on your interpretation must be given, if you know them. … If you make a theory, for example, and advertise it, or put it out, then you must also put down all the facts that disagree with it, as well as those that agree with it."
   > 演讲结尾："I have just one wish for you — the good luck to be somewhere where you are free to maintain the kind of integrity I have described, and where you do not feel forced by a need to maintain your position in the organization, or financial support, or so on, to lose your integrity. May you have that freedom."
3. 【他说过】【一手】1964 意大利 Galileo Symposium 演讲 "What is and What Should be the Role of Scientific Culture in Modern Society"：
   > "Science is a way of trying not to fool yourself. The first principle is that you must not fool yourself, and you are the easiest person to fool."
   > 收于《The Pleasure of Finding Things Out》(1999)。**注意**：这句话比 1974 年演讲早 10 年。
4. 【他说过】【一手】《What Do You Care What Other People Think?》(1988) "Afterthoughts," p.217-218：
   > "The only way to have real success in science, the field I'm familiar with, is to describe the evidence very carefully without regard to the way you feel it should be. If you have a theory, you must try to explain what's good and what's bad about it equally. In science, you learn a kind of standard integrity and honesty."
5. 【他说过】【一手】1986 Rogers Commission 报告 Appendix F（挑战者号调查）：
   > "For a successful technology, reality must take precedence over public relations, for nature cannot be fooled."
   > 出处：`http://history.nasa.gov/rogersrep/v2appf.htm`（本报告为官方文件，其中该附录系 Feynman 本人署名章节）
6. 【他说过】【一手】同一演讲中他自嘲 Millikan 油滴实验后人的"数字向权威值收敛"现象，并说：
   > "this long history of learning how to not fool ourselves — of having utter scientific integrity — is, I'm sorry to say, something that we haven't specifically included in any particular course that I know of. We just hope you've caught on by osmosis."

---

### 论点 D：无知、怀疑、不确定性是进步的前提（不是障碍）
**出现次数：6 次以上，1955 → 1981，是他最稳定的一条。**

1. 【他说过】【一手】"The Value of Science," 美国国家科学院演讲（1955 秋）：
   > "We have found it of paramount importance that in order to progress we must recognize our ignorance and leave room for doubt. Scientific knowledge is a body of statements of varying degrees of certainty — some most unsure, some nearly sure, but none *absolutely* certain. … Our freedom to doubt was born out of a struggle against authority in the early days of science. … Permit us to question — to doubt, that's all — not to be sure."
   > 出处：Caltech 档案扫描 `https://calteches.library.caltech.edu/1575/1/Science.pdf`（原载 *Engineering and Science* Vol.XIX, 1955-12）；另收于《What Do You Care…》(1988) 与《The Pleasure of Finding Things Out》(1999)
2. 【他说过】【一手】同篇：
   > "The idea that no one really knew how to run a government led to the idea that we should arrange a system by which new ideas could be developed, tried out, and tossed out if necessary, with more new ideas brought in — a trial and error system."
   > "If we want to solve a problem that we have never solved before, we must leave the door to the unknown ajar."
   > "to teach how doubt is not to be feared but welcomed and discussed; and to demand this freedom as our duty to all coming generations."
3. 【他说过】【一手】1964 Galileo Symposium 演讲：
   > "We absolutely must leave room for doubt or there is no progress and there is no learning. There is no learning without having to pose a question. And a question requires doubt. People search for certainty. But there is no certainty. … It is possible to live and not know."
4. 【他说过】【一手】1966 NSTA 演讲 "What is Science?"（原刊 *The Physics Teacher* 7(6), 1969, p.313-320）：
   > "Science alone of all the subjects contains within itself the lesson of the danger of belief in the infallibility of the greatest teachers of the preceding generation."
   > "Science is the belief in the ignorance of experts."
   > "When someone says 'Science teaches such and such,' he is using the word incorrectly. Science doesn't teach it; experience teaches it. … you have as much right as anyone else, upon hearing about the experiments (but we must listen to all the evidence), to judge whether a reusable conclusion has been arrived at."
   > 出处：`http://www.fotuva.org/feynman/what_is_science.html`；收于《The Pleasure of Finding Things Out》(1999) p.186-187
5. 【他说过】【一手】1981 BBC Horizon 访谈（收于 Sykes《No Ordinary Genius》p.239；另见《The Pleasure of Finding Things Out》）：
   > "I can live with doubt, and uncertainty, and not knowing. I think it's much more interesting to live not knowing than to have answers which might be wrong. … I don't have to know an answer. I don't feel frightened by not knowing things, by being lost in the mysterious universe without having any purpose — which is the way it really is, as far as I can tell. Possibly. It doesn't frighten me."
6. 【他说过】【一手】《The Meaning of It All》lecture II "The Uncertainty of Values"：
   > "It is in the admission of ignorance and the admission of uncertainty that there is a hope for the continuous motion of human beings in some direction that doesn't get confined, permanently blocked…"
   > "The fact that you are not sure means that it is possible that there is another way someday."

---

### 论点 E：反权威、反名相、反"专家"（有结构的怀疑，不是虚无）
**出现次数：5 次以上。**

1. 【他说过】【一手】《What Do You Care What Other People Think?》"What Do *You* Care What Other People Think?", p.28-29：
   > "Have no respect *whatsoever* for authority; forget who said it and instead look what he starts with, where he ends up, and ask yourself, 'Is it reasonable?'"
   > 他明确说这是从父亲那里学来的（对 Descartes 的怀疑）。
2. 【他说过】【一手】《Surely You're Joking》Part 5, "The 7 Percent Solution," p.255：
   > "Since then I never pay attention to anything by 'experts'. I calculate everything myself."
   > 下一句："I'll never make that mistake again, reading the experts' opinions. Of course, you only live one life, and you make all your mistakes, and learn what not to do, and that's the end of you."
3. 【他说过】【一手】《The Meaning of It All》lecture III "This Unscientific Age"——他给出的**识别伪专家的可操作技巧**：
   > "The first one has to do with whether a man knows what he is talking about, whether what he says has some basis or not. And my trick that I use is very easy. If you ask him intelligent questions — that is, penetrating, interested, honest, frank, direct questions on the subject, and no trick questions — then he quickly gets stuck. It is like a child asking naive questions. If you ask naive but relevant questions, then almost immediately the person doesn't know the answer, if he is an honest man."
4. 【他说过】【一手】《Surely You're Joking》Part 4, "O Americano, Outra Vez!", p.218（评巴西教育）：
   > "I said that I couldn't see how anyone could be educated by this self-propagating system in which people pass exams, and teach others to pass exams, but nobody knows anything."
5. 【他说过】【一手】"New Textbooks for the 'New' Mathematics," *Engineering and Science* 28(6) (1965-03) p.14：
   > "The real problem in speech is not precise language. The problem is clear language. … It is really quite impossible to say anything with absolute precision, unless that thing is so abstracted from the real world as to not represent any real thing."
   > 出处：`http://calteches.library.caltech.edu/2362/1/feynman.pdf`
6. 【他说过】【一手】《The Meaning of It All》lecture III：他把当时心理学/精神分析直接称作现代版的"巫医"（witch doctors），并据 Goodstein 记载，说到这里整个心理系当场退场。

**【我推断｜推测】** E 与 D 不是两条，而是同一枚硬币：D 是「对自己保留无知」，E 是「对外拒绝权威」。它们的共同操作接口是 §1-A 的"重建判据"和"幼稚但相关的问题"。建议合并为一个「怀疑的双重结构」心智模型。

---

### 论点 F：自然的想象力大于人的想象力；不要告诉自然它该怎样
**出现次数：4 次。**

1. 【他说过】【一手】"The Value of Science" (1955)：
   > "The imagination of nature is far, far greater than the imagination of man."
2. 【他说过】【一手】*The Character of Physical Law* ch.7 "Seeking New Laws," p.162：
   > "Nature's imagination far surpasses our own."
3. 【他说过】【一手】1979 Sir Douglas Robb Lectures（Auckland），Lecture 1 "Photons: Corpuscles of Light"：
   > "*We* are not to tell Nature what she's gotta be! … She's clever. She's always got better imagination than we have, and she finds a cleverer way to do it than we have thought of."
   > 视频存档：`https://www.vega.org.uk/video/programme/45`
4. 【他说过】【一手】*QED* (1985) p.10：
   > "The theory of quantum electrodynamics describes Nature as absurd from the point of view of common sense. And it agrees fully with experiment. So I hope you accept Nature as She is — absurd."
   > 同书 p.9："Will you *understand* what I'm going to tell you? … No, you're not going to be able to understand it. … That is because *I* don't understand it. Nobody does."
5. 【他说过】【一手】*The Character of Physical Law* ch.6, p.129：
   > "Do not keep saying to yourself, if you can possibly avoid it, 'But how can it be like that?' because you will get 'down the drain', into a blind alley from which nobody has yet escaped. Nobody knows how it can be like that."

---

### 论点 G：局部蕴含整体 / 简单性是真理的信号 / 一条定律在别处比你推导出它更成立
**出现次数：4 次。**

1. 【他说过】【一手】*The Character of Physical Law* ch.1 "The Law of Gravitation," p.34：
   > "Nature uses only the longest threads to weave her patterns, so each small piece of her fabric reveals the organization of the entire tapestry."
2. 【他说过】【一手】同书 ch.2 "The Relation of Mathematics to Physics"（守恒定律/角动量例子）：
   > "We can deduce, often, from one part of physics like the law of gravitation, a principle which turns out to be much more valid than the derivation. This doesn't happen in mathematics, that the theorems come out in places where they're not supposed to be!"
   > "while we don't know all the laws, we can use some to make guesses at theorems which extend beyond the proof."
3. 【他说过】【一手】*The Feynman Lectures on Physics* Vol. I, lecture 1, §1-2, p.1-2（原子假说）——他把"最少字数承载最多信息"当作选择判据：
   > "If, in some cataclysm, all of scientific knowledge were to be destroyed, and only one sentence passed on to the next generation of creatures, what statement would contain the most information in the fewest words? I believe it is the *atomic hypothesis*… In that one sentence, you will see, there is an *enormous* amount of information about the world, if just a little imagination and thinking are applied."
4. 【他说过】【一手】*The Character of Physical Law* ch.2, p.45：
   > "[T]he total amount that a physicist knows is very little. He has only to remember the rules to get him from one place to another…"
5. 【他说过】【一手】1981 Horizon 访谈（Sykes《No Ordinary Genius》p.251-252）：
   > "People say to me, 'Are you looking for the ultimate laws of physics?' No, I'm not. I'm just looking to find out more about the world… And therefore when we go to investigate we shouldn't pre-decide what it is we are trying to do except to find out more about it."

**矛盾（记录，不调和）**：(1)(2)(3) 断言自然是高度统一、可由碎片反推整体的；但 *QED* p.149-150 他自己给出相反的自嘲解释——"Why are the theories of physics so similar in their structure? … The first is the limited imagination of physicists… it's not because Nature is really similar; it's because the physicists have only been able to think of the same damn thing, over and over again." 见 §5-D。

---

### 论点 H：乐趣 / 玩 / "找出来的快感"是第一驱动力
**出现次数：5 次以上。**

1. 【他说过】【一手】1981 BBC Horizon 访谈（Sykes《No Ordinary Genius》p.82）：
   > "I don't like honors. … I've already got the prize: the prize is the pleasure of finding the thing out, the kick in the discovery, the observation that other people use it. Those are the real things."
2. 【他说过】【一手】*Feynman Lectures on Computation* Ch.1：
   > "Do them for the fun of it. That's how to learn the knack of doing things when you have to do them. … when you play with this sort of problem as a kid, and you haven't been shown the answer… it's fun trying to figure out how to do it. Then, as you go into adulthood, you develop a certain confidence that you can discover things; but if they've already been discovered, that shouldn't bother you at all. What one fool can do, so can another, and the fact that some other fool beat you to it shouldn't disturb you."
3. 【他说过】【一手】1959-12-29 "There's Plenty of Room at the Bottom"（APS 加州理工）：
   > "Let's have a competition between laboratories. Let one laboratory make a tiny motor which it sends to another lab which sends it back with a thing that fits inside the shaft of the first motor." 以及结尾设立两个 $1,000 奖金挑战（一个给"把一页书缩小到 1/25,000 仍可用电子显微镜读出"，一个给"1/64 英寸立方的可运转电动机"），并说 "I do not expect that such prizes will have to wait very long for claimants."
   > 出处：原载 *Engineering and Science* Vol.XXIII No.5 (1960-02) p.22-36；转录副本 `https://courses.cs.duke.edu/spring04/cps296.4/papers/Feynman59.pdf`、`https://physics.bme.hu/sites/physics.bme.hu/files/users/BMETE11MF58_kov/Feynman_Plenty_of_room.pdf`；Caltech 后续报道 `https://calteches.library.caltech.edu/597/2/Tale.pdf`（两个奖金分别于 1960-11-28 由 William McLellan 领取、1985-11 由 Tom Newman 领取）
4. 【他说过】【一手】*The Feynman Lectures on Physics* Vol. I, lecture 22 §22-1 p.22-1：
   > "the real reason is that the subject is enjoyable, and although we humans cut nature up in different ways, and we have different courses in different departments, such compartmentalization is really artificial, and we should take our intellectual pleasures where we find them."
5. 【他说过】【一手】1979 年 *Omni* 访谈 "The Smartest Man in the World" p.203：
   > "I don't know anything, but I do know that *everything is interesting* if you go into it deeply enough."
6. 【他说过】【一手】1988 去世前两周访谈中谈图瓦（Sykes《No Ordinary Genius》p.236），他拒绝别人给他的图瓦之行加哲学意义：
   > "It's a game. It's not serious. It doesn't involve some deep philosophical point of view about authority or anything. It's just the fun of having an adventure… We haven't any deep understanding of what we're doing. If we tried to understand what we're doing, we'd go nutty."

---

### 论点 I：从不同角度看同一个问题 / 保持多套工具与多套表征
**出现次数：3 次以上（这条常被"费曼技巧"叙事吞掉，但它确实是他的原话）。**

1. 【他说过】【一手】*The Character of Physical Law* ch.7 "Seeking New Laws," p.168：
   > "Therefore psychologically we must keep all the theories in our heads, and every theoretical physicist who is any good knows six or seven different theoretical representations for exactly the same physics."
2. 【他说过】【一手】《Surely You're Joking》Part 1（章节名即 "A Different Box of Tools"）：
   > "That book also showed how to differentiate parameters under the integral sign — it's a certain operation. It turns out that's not taught very much in the universities; they don't emphasize it. But I caught on how to use that method, and I used that one damn tool again and again. … So I got a great reputation for doing integrals, only because my box of tools was different from everybody else's, and they had tried all their tools on it before giving the problem to me."
   > 来源：高中物理老师 Abram Bader 给的 Frederick S. Woods《Advanced Calculus》(1926)；此前他自学的底子是《Calculus for the Practical Man》。【二手】Wikipedia/Leibniz integral rule 条目与 HuffPost 转录均引此段，页码定位在 Part 1。
3. 【他说过】【一手】*The Feynman Lectures on Physics* Vol. II, lecture 2, §2-1 "Understanding physics," p.2-1：
   > "The physicist needs a facility in looking at problems from several points of view. … On the other hand, none of the heuristic models, such as field lines, is really adequate and accurate for all situations. There is only one precise way of presenting the laws, and that is by means of differential equations. … If you have learned the differential equations you can always go back to them. There is nothing to unlearn."
4. 【他说过】【一手】*The Feynman Lectures on Physics* Vol. II, lecture 12, p.12-1：**"The same equations have the same solutions."**（这是他最著名的方法论短句之一，也是"类比/映射"解法的正式表述）
5. 【他说过】【一手】1988 遗著 *Feynman's Tips on Physics* 相关表述："The problem of how to deduce new things from old, and how to solve problems, is really very difficult to teach, and I don't really know how to do it."【二手】sobrief 转录，需以原书核对。

---

## 2. 他自创的概念 / 说法（严格区分两类）

### 2.1 专业物理贡献（**不是**思维层说法，列出仅为划清边界）
| 术语 | 性质 | 出处 |
|---|---|---|
| Feynman diagram（费曼图） | 计算工具/表征法 | 1948-49 系列论文，*Phys. Rev.* |
| Path integral formulation（路径积分） | 理论构造 | 1942 Princeton 博士论文（导师 J. A. Wheeler）+ 1948 *Rev. Mod. Phys.* 20, 367 |
| Bethe–Feynman formula | 工程公式 | Los Alamos, 1943-45 |
| Parton model（部分子模型） | 物理模型 | 1969 前后 |
| Feynman–Kac、Hellmann–Feynman 定理等 | 数学/物理结果 | — |

> 这些**不应**进入心智模型库。它们是他思维的产物，不是他的思维规则。

### 2.2 思维层面的自创说法（这才是本维度要的）
| 说法 | 一手出处 | 出现/复现次数 | 归属 |
|---|---|---|---|
| **"cargo cult science"** | 1974 Caltech 毕业演讲（Caltech 档案原件 `calteches.library.caltech.edu/51/2/CargoCult.htm`）；收于《Surely You're Joking》p.341-346 | 1 次原创，后被他本人反复引用（1985 书、1974 演讲） | 【他说过】【一手】 |
| **"What I cannot create, I do not understand."** | 1988 去世时办公室黑板（Caltech 档案照片）。**注意**：这不是演讲或书里的句子，是他留给自己的便条 | 1 次（但语义在 1946/1974/1983-86/1996 多次复现，见 §1-A） | 【他说过】【一手】 |
| **"the first principle is that you must not fool yourself — and you are the easiest person to fool"** | 1964 Galileo Symposium（早于 1974 演讲 10 年）与 1974 Cargo Cult 演讲各 1 次 | ≥2 次原文重复 | 【他说过】【一手】 |
| **"science is the belief in the ignorance of experts"** | 1966 NSTA 演讲 "What is Science?"（*The Physics Teacher* 7(6), 1969, p.313-320）；收于《The Pleasure of Finding Things Out》p.187 | 1 次原创 + 大量复述 | 【他说过】【一手】 |
| **"the pleasure of finding things out"** | 1981 BBC Horizon 访谈；成为 1999 文集书名 | 与 1988 遗言、"I don't like honors" 同源 | 【他说过】【一手】 |
| **"Nature uses only the longest threads to weave her patterns…"** | *The Character of Physical Law* ch.1, p.34 | 1 次（语义在 QED/FLP 复现） | 【他说过】【一手】 |
| **"There's plenty of room at the bottom"** | 1959-12-29 APS 演讲（*Engineering and Science* 1960-02） | 1 次 | 【他说过】【一手】 |
| **"Nature isn't classical, dammit…"** | "Simulating Physics with Computers," *Int. J. Theor. Phys.* 21 (1982) p.467-488，末句在 p.486 | 1 次 | 【他说过】【一手】 |
| **"a different box of tools"** | 《Surely You're Joking》Part 1 章节标题 | 与 ch.7 "six or seven different theoretical representations" 呼应 | 【他说过】【一手】 |
| **"The same equations have the same solutions."** | FLP Vol. II, lecture 12, p.12-1 | 1 次（但整本书在用） | 【他说过】【一手】 |
| **"The exception tests the rule" / "The exception proves that the rule is wrong"** | 《The Meaning of It All》lecture I（1963-04） | 1 次 | 【他说过】【一手】 |
| **"I have a limited intelligence and I've used it in a particular direction."** | 《The Pleasure of Finding Things Out》p.2-3（1981 Horizon 转录） | 1 次 | 【他说过】【一手】 |
| **"for a successful technology, reality must take precedence over public relations, for nature cannot be fooled"** | Rogers Commission Report (1986) Appendix F | 1 次 | 【他说过】【一手】 |
| **"Notebook of Things I Don't Know About"** | 【别人说他】【二手】James Gleick《Genius》记载他在 MIT 备考研时开了一本笔记，首页写此标题 | — | 需以 Gleick 原书页码核对 |

---

## 3. 智识谱系：他明确说过受谁影响，以及他推荐什么

### 3.1 父亲 Melville Feynman（最常被他自陈的来源）
- 【他说过】【一手】《What Do You Care What Other People Think?》"The Making of a Scientist," p.14：鸟的故事（见 §1-A-4）。
- 【他说过】【一手】Sykes《No Ordinary Genius》p.28：
  > "The most important thing I found out from [my father] is that if you asked any question and pursued it deeply enough, then at the end there was a glorious discovery of a general and beautiful kind."
- 【他说过】【一手】《What Do You Care…》p.28-29：反权威那条（"Have no respect whatsoever for authority…"）他明说是对 Descartes 的反应、从父亲那儿学的。
- 【他说过】【一手】1979 *Omni* 访谈 p.194（收于《The Pleasure of Finding Things Out》）：
  > "What one fool can do, another fool can."（他引用自己那本微积分书上的题词，用来反对"只有少数怪人能懂数学"的说法）
- 【别人说他】【二手】Gribbin & Gribbin《Richard Feynman: A Life in Science》转述：父亲在幼儿高脚椅时期就用彩色浴室瓷砖摆图案教他序列/比例；把恐龙"25 英尺高、头 6 英尺宽"翻译成"头能伸到我们家二楼窗户、比窗户还宽"。以及那个关键回答——关于 wagon 里的球："That, nobody knows. The general principle is that things which are moving tend to keep on moving… This tendency is called 'inertia', but nobody knows why it's true."
  > **这条极重要**：父亲给他的不是"答案"而是"答案的边界"（给定律命名 ≠ 懂了为什么）。【我推断｜推测】这正是 §1-A 与 §1-D 的共同源头。
- 【别人说他】【二手】高中物理老师 Abram Bader 给他 Woods《Advanced Calculus》，并向他介绍"最小作用量原理"。Feynman 回忆（据 Wikiwand/中文百科转述，**需以《Surely You're Joking》原文核对**）："他只是解说，他并没有证明任何东西……我随即为之倾倒，能以这样不寻常的方式来表达一个法则，简直是个不可思议的奇迹。"
  > 注意：Wikiwand 与 baike.com 均为百科站，此处仅作线索，**未采信**，待查原文。

### 3.2 Dirac（他明确称为"我的英雄"）
- 【他说过】【一手】1986 Dirac Memorial Lecture "Elementary Particles and the Laws of Physics"（收于 Feynman & Weinberg, *Elementary Particles and the Laws of Physics*, CUP, 1987/1999, p.1），**开场即**：
  > "When I was a young man, Dirac was my hero. He made a new breakthrough, a new method of doing physics. He had the courage to simply guess at the form of an equation, the equation we now call the Dirac equation, and to try to interpret it afterwards."
  > 出处核验：Sotheby's 2022 拍品说明（含书目：`Feynman, "The Reason for Antiparticles," in Feynman & Weinberg, op. cit., p.1`）与 roughlydaily 转录一致。
- 【他说过】【一手】Nobel Lecture (1965-12-11) 原文：
  > "This I gathered from books like those of Heitler and Dirac. I was inspired by the remarks in these books; not by the parts in which everything was proved and demonstrated carefully and calculated, because I couldn't understand those very well. At the young age what I could understand were the remarks about the fact that this doesn't make any sense, and the last sentence of the book of Dirac I can still remember, 'It seems that some essentially new physical ideas are here needed.' So, I had this as a challenge and an inspiration. I also had a personal feeling, that since they didn't get a satisfactory answer to the problem I wanted to solve, I don't have to pay a lot of attention to what they did do."
  > 出处：`https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/`（一手全文）
- 【他说过】【一手】*The Character of Physical Law* ch.2, p.58：
  > "Dirac discovered the correct laws for relativity quantum mechanics simply by guessing the equation. The method of guessing the equation seems to be a pretty effective way of guessing new laws."
- 【别人说他】【二手】Sotheby's 拍品说明：Feynman 高中二年级时就读了 Dirac《The Principles of Quantum Mechanics》（他批注过的副本 2019 年以 $87,500 拍出）；Wigner 评价 "He is a second Dirac, only this time human."（引自 Gleick《Genius》p.184）

### 3.3 Wheeler / Bethe / von Neumann
- **Wheeler**：【别人说他】【二手】Princeton 博士导师（1942，论文 *The Principle of Least Action in Quantum Mechanics*）。Britannica：`https://www.britannica.com/biography/Richard-Feynman`
- **Bethe**：【他说过】【一手】《Surely You're Joking》Part 3（Los Alamos 章节），他讲自己"不知道对方是谁"所以敢直说：
  > "when I hear about physics, I just think about physics, and I don't know who I'm talking to, so I say dopey things like, 'no no you're wrong,' or 'you're crazy.' But it turns out that's exactly what he [Bethe] needed." 以及 "I was always dumb in that way… I never knew who I was talking to. I was always worried about the physics. If the idea looked lousy, I said it looked lousy."
  > 【二手】HuffPost / dltn.io 转录，页码需以原书核对。
- **von Neumann**：【他说过】【一手】《Surely You're Joking》Part 3, "Los Alamos from Below," p.132：
  > "[John] von Neumann gave me an interesting idea: that you don't have to be responsible for the world that you're in. So I have developed a very powerful sense of social irresponsibility as a result of von Neumann's advice. It's made me a very happy man ever since."
  > ⚠️ 这句是反讽/玩笑，不能当字面信念读。【我推断｜推测】它揭示的是他对"责任边界"的自我意识，而非不负责任。

### 3.4 他推荐的书 / 学习材料（明确见于文本）
- Woods《Advanced Calculus》(1926) —— 给了他"积分号下求导"这一工具（见 §1-I-2）。
- 《Calculus for the Practical Man》—— 高中自学底子。
- 《Encyclopaedia Britannica》—— 童年与父亲共读（【别人说他】【二手】多处转述）。
- Dirac《The Principles of Quantum Mechanics》、Heitler 的量子力学书 —— Nobel 演讲自陈。
- 【他说过】【一手】1967-01-04 致印度教师 Ashok Arora 的信（《Perfectly Reasonable Deviations…》p.230）：
  > "Do not read so much, look about you and think of what you see there."
- 【他说过】【一手】1966-02-03 致弟子 Koichi Mano 的信（同书，另见 Freeman Dyson 在 *NYRB* 2005-10-20 书评 "Wise Man"）：
  > "The worthwhile problems are the ones you can really solve or help solve, the ones you can really contribute something to. … No problem is too small or too trivial if we can really do something about it."

### 3.5 【我推断｜推测】谱系总结
四条独立输入汇成同一条河流：(a) 父亲给的「名字 ≠ 懂」+「追问到底会有普遍发现」；(b) Bader 给的「最小作用量 = 不解释却普遍成立的表达方式」（→ 后来他对"定律比推导更成立"的执着，§1-G-2）；(c) Dirac 给的「先猜方程、再解释」（→ §1-B 的 guess 步骤）；(d) Woods 给的「非标准工具」（→ §1-I）。共同结构是：**接受一个最小支点（原理/方程/工具），然后自己把其余全部重建。**

---

## 4. 系统性长文中的思维方法（逐篇）

### 4.1 "There's Plenty of Room at the Bottom" (1959-12-29, APS @ Caltech)
- 【他说过】【一手】方法论骨架："I am not inventing anti-gravity, which is possible someday only if the laws are not what we think. **I am telling you what could be done if the laws are what we think; we are not doing it simply because we haven't yet gotten around to it.**"
  > ⚠️ 这是他最纯粹的思维动作之一：**把"物理上允许"与"工程上已做到"严格切开**，只在前者上做推理。
- 【他说过】【一手】量化直觉：大头针头放大 25,000 直径 = 大英百科全书全部页面面积；一个点仍含 1,000 个原子；全世界所有书的信息可写进 1/200 英寸宽的立方体。"So there is plenty of room at the bottom! Don't tell me about microfilm!"
- 【他说过】【一手】"The Marvelous Biological System" 一节的核心论点：生物"做"得到而人类"造"不出，说明这不是物理定律禁止的，只是我们不会。
- 【我推断｜推测】1959 与 1982（量子计算）两篇是同一个模板：**先证明 X 不被物理定律禁止（只是没人做），再把 X 变成一个可招标的公开问题（1959 的 $1,000 奖金 / 1982 的"那就造一台量子计算机"）。** 建议作为独立心智模型候选。

### 4.2 "Simulating Physics with Computers" (*IJTP* 21, 1982, p.467-488)
- 【他说过】【一手】p.486 末句：
  > "…I'm not happy with all the analyses that go with just the classical theory, because nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical, and by golly it's a wonderful problem, because it doesn't look so easy."
- 【他说过】【一手】p.471（关于他是否认为量子力学有"真正的问题"）：
  > "It has not yet become obvious to me that there's no real problem. I cannot define the real problem, therefore I suspect there's no real problem, but I'm not sure there's no real problem."
  > 【我推断｜推测】这条比它对量子力学的字面内容更值钱——它是他处理"我不确定我是否真的有问题"的元规则：**承认无法定义问题，因此降低对问题存在性的置信度，但不降到零。**

### 4.3 "The Value of Science" (1955)
见 §1-D。另外：
- 【他说过】【一手】"Scientific knowledge is an enabling power to do either good or bad — but it does not carry instructions on how to use it." + 檀香山佛寺谚语 "To every man is given the key to the gates of heaven; the same key opens the gates of hell."
- 【他说过】【一手】"This is not yet a scientific age."（对公众科学素养的判断）
- 【他说过】【一手】长篇散文诗（"I stand at the seashore, alone, and start to think… I, a universe of atoms, an atom in the universe."）——他唯一一次用诗歌形式处理同一主题。

### 4.4 "Cargo Cult Science" (1974)
见 §1-C。补一条被低估的段落——他对**教学法**的判断：
- 【他说过】【一手】"It is very dangerous to have such a policy in teaching — to teach students only how to get certain results, rather than how to do an experiment with scientific integrity."

### 4.5 《The Feynman Lectures on Physics》(1961-63 授课，1963-65 出版)
- 【他说过】【一手】Vol. I, lecture 2 §2-1 p.2-1（"理解"的定义）：
  > "What do we mean by 'understanding' something? We can imagine that this complicated array of moving things which constitutes 'the world' is something like a great chess game being played by the gods, and we are observers of the game. We do not know what the rules of the game are; all we are allowed to do is to *watch* the playing. Of course, if we watch long enough, we may eventually catch on to a few of the rules. *The rules of the game* are what we mean by *fundamental physics*."
- 【他说过】【一手】Vol. I, lecture 4 §4-1 p.4-2：
  > "It is important to realize that in physics today, we have no knowledge what energy *is*."
  > 【我推断｜推测】这是 §1-A 的一个反面实例：他愿意明确宣布"我们不知道能量是什么"，即**拒绝用名字冒充理解**。
- 【他说过】【一手】Vol. I, lecture 8 §8-2 p.8-2：
  > "We cannot define *anything* precisely. If we attempt to, we get into that paralysis of thought that comes to philosophers…"
- 【他说过】【一手】Vol. II, lecture 26 §26-2 p.26-2（反"少数假设推出大量结论"）：
  > "Whenever you see a sweeping statement that a tremendous amount can come from a very small number of assumptions, you always find that it is false. There are usually a large number of implied assumptions that are far from obvious if you think about them sufficiently carefully."
- 【他说过】【一手】Vol. III, lecture 18 §18-3 p.18-9：
  > "The 'paradox' is only a conflict between reality and your feeling of what reality 'ought to be.'"
- 【他说过】【一手】Vol. I, lecture 35 §35-1 p.35-1（反学科分割）：
  > "the separation of fields, as we have emphasized, is merely a human convenience, and an unnatural thing. Nature is not interested in our separations…"
- 【他说过】【一手】Vol. III "Feynman's Epilogue" p.21-19（全书最后一句）：
  > "Perhaps you will not only have some appreciation of this culture; it is even possible that you may want to join in the greatest adventure that the human mind has ever begun."

---

## 5. 矛盾与张力（记录，不调和）

### A. 《费曼物理学讲义》成败：他自己的评价 vs 同事的反证
- 【他说过】【一手】Feynman 1963 年口授的 Preface（三卷通用）：
  > "My own point of view — which, however, does not seem to be shared by most of the people who worked with the students — is pessimistic. I don't think I did very well by the students. When I look at the way the majority of the students handled the problems on the examinations, I think the system is a failure."
  > （另引 Gibbon："The power of instruction is seldom of much efficacy except in those happy dispositions where it is almost superfluous."）
- 【别人说他】【一手回忆】Matthew Sands（课程共同组织者、Vol. I-III 编辑之一）在 *Physics Today* (2005-04) "Capturing the Wisdom of Feynman" 与《Feynman's Tips on Physics》回忆录中说：这句序是在得知第二年期末平均分约 65%、心情低落时**对着录音机即兴口授**的，并非深思熟虑；Sands 明确写 "I have often regretted that I had arranged for him to make a preface in this way, because I do not think that this was a very considered judgment."
- 【别人说他】【二手】David Goodstein & Neugebauer 在 1989 纪念版前言中称"本科生出席率惊人下降、教室被研究生和教师填满、很多学生害怕这门课"；**但 Sands 直接反驳**：Goodstein 当时还未到 Caltech，Neugebauer 的"教室里没本科生了"是当年的玩笑被误当成记忆；Sands 本人大多数课坐在后排，记得约 20% 学生不来（大班课的常态），并举证学生正面反馈（半年后仍能复述内容；1996 诺奖得主 Douglas Osheroff 说他的物理直觉大多来自这门课）。
- **不调和**：一手文本（Feynman 自评悲观）与一手回忆（Sands 说这是情绪化口授）冲突；二手统计（Goodstein/Neugebauer）又被另一位一手当事人推翻。我保留三方陈述，不做裁决。

### B. 对待"别人的已有工作"：轻视 vs 重视
- 【他说过】【一手】Nobel Lecture 1965："I also had a personal feeling, that since they didn't get a satisfactory answer to the problem I wanted to solve, I don't have to pay a lot of attention to what they did do."
- 【他说过】【一手】*Feynman Lectures on Computation* Ch.1："The other way, which is also valuable, is to read carefully how someone else did it. … Finally, after you've figured out how to do it you read how they did it and find out how dumb your solution is and how much more clever and efficient theirs is!"
- **不调和**：1965 年他主张"跳过文献"，1983-86 年他主张"先自己解、再读别人的、然后发现自己多笨"。两者相差二十年，可能是立场变化，也可能是语境差异（前者针对"权威没解决的问题"，后者针对"已解决的问题"）。我没有证据判断是哪一种。

### C. 实验裁判 vs 美/简洁作为真理信号
见 §1-B 结尾。FLP/《The Meaning of It All》说观察是唯一裁判；《The Character of Physical Law》ch.7 p.171 说"You can recognize truth by its beauty and simplicity"，并说"you can know when you are right way ahead of checking all the consequences"。他从未给出两者的优先级。

### D. 自然统一性 vs 物理学家的想象力贫乏
见 §1-G 结尾。ch.1 p.34 的"长线织锦"是本体论乐观；*QED* p.149-150 的"limited imagination of physicists"是认识论自嘲。两句话都出自他自己，且都很认真。

### E. 数学的地位
- 【他说过】【一手】*The Character of Physical Law* ch.2, p.58："If you want to learn about nature, to appreciate nature, it is necessary to understand the language that she speaks in."；"Mathematics is not just a language. Mathematics is a language plus reasoning."
- 【他说过】【一手】同章 p.58（几乎同一页）："I have often made the hypotheses that ultimately physics will not require a mathematical statement, that in the end the machinery will be revealed, and the laws will turn out to be simple, like the chequer board with all its apparent complexities."
- **不调和**：他在同一章里既说自然是数学语言的、必需掌握，又说物理最终可能不需要数学表述。注意第二句他自己标为"hypotheses"。

### F. 荣誉与"不在乎别人怎么想"
- 【他说过】【一手】1981 Horizon："I don't like honors."；《Surely You're Joking》p.172："You have no responsibility to live up to what other people think you ought to accomplish."
- 【别人说他】【二手】Gell-Mann 在 *Physics Today* (1989-02) "Dick Feynman — The Guy in the Office Down the Hall" 中批评他"耗费大量时间精力打造关于自己的趣闻轶事"，且故事里"他一般都是英雄人物"。
- **不调和**：自我叙事（不在乎）与同事观察（非常在乎人设）冲突。两条都保留。

### G. 黑板那句话的性质
【我推断｜推测】"What I cannot create, I do not understand" 常被当成他的"方法论宣言"，但它其实是**黑板上的私人便条**（Preskill 记载：1986-87 年他与学生的每周讨论中，Feynman 反复对学生说这句话，要求他们不许查文献自己解）。即：这句话的语境是**对学生的要求**，不是对自己的描述。这改变了它的语义重量——它是一条他反复施加于他人的纪律。
- 【别人说他】【二手/准一手】John Preskill, "Quantum computing 40 years later"（CaltechAUTHORS `https://authors.library.caltech.edu/records/d3hjb-yrc95/files/2106.10522.pdf`）："Feynman told the students 'We gotta know how to solve every problem that has been solved,' and he urged them to solve the problems on their own because 'What I cannot create I do not understand.' … he told everyone to solve it without looking up any references."（Preskill 是当事人，他自己的学生 Sandip Trivedi 参与其中。）

---

## 6. 存疑语录，不采纳（查不到一手出处，或已被证伪）

| # | 流传的语录 | 判定 | 依据 |
|---|---|---|---|
| 1 | **"Shut up and calculate!"** | ❌ 不采纳。大概率是 N. David Mermin 自创 | Mermin 本人, "Could Feynman Have Said This?", *Physics Today* (2004-05) p.10；最早出现于 Mermin 在 *Physics Today* (1989-04) p.9 的文字 |
| 2 | **"Physics is like sex: sure, it may give some practical results, but that's not why we do it."** | ❌ 不采纳 | 不见于他的任何书或传记；Google Books 显示最早引用在 Robyn Williams《Scary Monsters and Bright Ideas》(2000) p.44，且与一条同样伪造的 Einstein 语录并列 |
| 3 | **"The philosophy of science is as useful to scientists as ornithology is to birds."** | ❌ 不采纳 | 常由 Brian Cox 归于他，但无一手出处；Wikiquote 列入 disputed |
| 4 | **"If you can't explain it simply, you don't understand it well enough."** | ❌ 不采纳（Einstein/Feynman 都不可靠归因） | 多个来源同时把它归给 Einstein 和 Feynman，说明是游走型伪引语 |
| 5 | **"Religion is a culture of faith; science is a culture of doubt."** | ⚠️ 存疑 | 广泛流传，但我在一手文本中未找到该句式；他的可核验表述是 "Science is a way of trying not to fool yourself" 与 "freedom to doubt"，语义相近但不同形 |
| 6 | **"I was an ordinary person who studied hard. There are no miracle people."** | ⚠️ 存疑 | 仅见于语录聚合站与媒体转述（如 Times of India 2026），无一手出处。他可核验的相关表述是 "What one fool can do, another fool can"（引自自己的微积分书）与 "I have a limited intelligence and I've used it in a particular direction." |
| 7 | **"Dear Mrs. Chown, Ignore your son's attempts to teach you physics. Physics isn't the most important thing. Love is."** | ⚠️ 需修正 | Wikiquote 明确指出这是**误传的转述版**；原件照片上的文字是："Tell your son to stop trying to fill your head with science — for to fill your heart with love is enough!"（Sykes《No Ordinary Genius》p.161） |
| 8 | **"Feynman Technique"（四步学习法：选概念→讲给小孩→找缺口→简化）** | ❌ 不是他的 | 名称最早见于 Scott Young 2011-09 的博文 "Learn Faster with the Feynman Technique"；Farnam Street 2012-04 推出四步版本。费曼本人从未写下这套步骤。**可用的替代**：黑板句 + Goodstein 记录的"大一新生讲座测试" + *Feynman Lectures on Computation* Ch.1 的自述 |
| 9 | **"Scientists are explorers. Philosophers are tourists."** | ⚠️ 存疑 | 仅见于语录站标《The Quotable Feynman》p.113，无原始语境/时间。不采纳为核心论据 |
| 10 | **"You can always recognize truth by its beauty and simplicity."** | ✅ 可采纳但有版本差 | 一手出处为 *The Character of Physical Law* ch.7 p.171，原句是 "You can recognize truth by its beauty and simplicity."（无 "always"）。网络版多加 "always"，请以原书为准 |
| 11 | **"I'd hate to die twice. It's so boring."（遗言）** | ⚠️ 版本冲突 | Gleick《Genius》(1992) p.438 作 "I'd hate to die twice. It's so boring."；妹妹 Joan 回忆（Sykes《No Ordinary Genius》p.254）作 "This dying is boring."。两个版本并存，勿混用 |

**总原则**：凡是只在语录聚合站（azquotes / brainyquote / goodreads / quotepark / fixquotes / 各类 blog）出现、查不到书名+章节+页码或演讲名+日期的，一律不进心智模型库。

---

## 7. 来源清单

### 一手（他本人的文字/声音/手迹 + 机构原始存档）
| # | 来源 | URL |
|---|---|---|
| 1 | "Cargo Cult Science" (1974 Caltech 毕业演讲)，Caltech 档案原件 | `http://calteches.library.caltech.edu/51/2/CargoCult.htm` / `.pdf` |
| 2 | "The Value of Science" (1955, NAS)，Caltech 扫描件 | `https://calteches.library.caltech.edu/1575/1/Science.pdf` |
| 3 | "There's Plenty of Room at the Bottom" (1959) 转录（原载 *E&S* 1960-02, XXIII(5) p.22-36） | `https://courses.cs.duke.edu/spring04/cps296.4/papers/Feynman59.pdf`；`https://physics.bme.hu/sites/physics.bme.hu/files/users/BMETE11MF58_kov/Feynman_Plenty_of_room.pdf` |
| 4 | 两笔 $1,000 奖金的后续（Caltech *E&S*） | `https://calteches.library.caltech.edu/597/2/Tale.pdf` |
| 5 | "New Textbooks for the 'New' Mathematics" (*E&S* 28(6), 1965-03) | `http://calteches.library.caltech.edu/2362/1/feynman.pdf` |
| 6 | Nobel Lecture (1965-12-11) 全文 | `https://www.nobelprizes.org` 系：`https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/` |
| 7 | 1988 黑板照片（Caltech Archives & Special Collections） | `https://digital.archives.caltech.edu/collections/Images/1.10-29/` |
| 8 | Feynman Lectures 官方站（含 AIP 访谈引语页） | `https://www.feynmanlectures.caltech.edu/info/other/Alternate_Way_to_Handle_Electrodynamics.html` |
| 9 | Messenger Lectures 官方视频（*Character of Physical Law* 口语原版） | `https://www.youtube.com/watch?v=-2NnquxdWFk`（ch.7）；`https://www.feynmanlectures.caltech.edu/fml.html` |
| 10 | Sir Douglas Robb Lectures (1979, Auckland) 视频存档 | `https://www.vega.org.uk/video/programme/45` |
| 11 | *Feynman Lectures on Computation* Ch.1 全文 | `https://icourse.club/uploads/files/cdf0a91886c41581ea984e5ca0aacd57627cc604.pdf` |
| 12 | "Simulating Physics with Computers," *IJTP* 21 (1982) 467-488 | `https://www.cs.berkeley.edu/~christos/classics/Feynman.pdf` |
| 13 | "What is Science?" (1966 NSTA；*The Physics Teacher* 7(6), 1969, p.313-320) | `http://www.fotuva.org/feynman/what_is_science.html` |
| 14 | Rogers Commission Report (1986) Appendix F | `http://history.nasa.gov/rogersrep/v2appf.htm` |
| 15 | *The Feynman Lectures on Physics* (Vol. I/II/III) — 卷-讲-节-页定位 | `https://www.feynmanlectures.caltech.edu/` |
| 16 | 书籍（纸质/官方）：*The Character of Physical Law* (1965)、*QED* (1985)、*Surely You're Joking* (1985)、*What Do You Care What Other People Think?* (1988)、*The Pleasure of Finding Things Out* (1999)、*The Meaning of It All* (1999)、*Perfectly Reasonable Deviations from the Beaten Track* (2005)、*Feynman's Tips on Physics* (2005) | — |
| 17 | Sykes 编《No Ordinary Genius》(1994)（BBC Horizon 访谈转录） | — |
| 18 | Feynman & Weinberg, *Elementary Particles and the Laws of Physics* (CUP, 1987/1999) p.1 "The Reason for Antiparticles" | — |

### 二手（带定位的引语索引 / 权威传记 / 权威媒体 / 同行回忆）
| # | 来源 | URL |
|---|---|---|
| 19 | Wikiquote: Richard Feynman（带卷/章/页码，含 "Disputed and/or attributed" 专节） | `https://en.wikiquote.org/wiki/Richard_Feynman` |
| 20 | David Goodstein, "Richard P. Feynman, Teacher," *Physics Today* 42(2) (1989-02) p.70-75 | — |
| 21 | Matthew Sands, "Capturing the Wisdom of Feynman," *Physics Today* (2005-04) p.49；及《Feynman's Tips on Physics》回忆录 | `https://www.physicstoday.org/vol-58/iss-4/p49.shtml`（原始链接，已失效，经 phys-l 存档转录引用） |
| 22 | John Preskill, "Quantum computing 40 years later"（CaltechAUTHORS） | `https://authors.library.caltech.edu/records/d3hjb-yrc95/files/2106.10522.pdf` |
| 23 | *Physics Today* (2017-03) p.11, "How to teach me physics: Tradition is not always a virtue" | `https://fermatslibrary.com/s/how-to-teach-me-physics-tradition-is-not-always-a-virtue` |
| 24 | N. David Mermin, "Could Feynman Have Said This?", *Physics Today* (2004-05) p.10 | — |
| 25 | Murray Gell-Mann, "Dick Feynman — The Guy in the Office Down the Hall," *Physics Today* (1989-02) | — |
| 26 | James Gleick, *Genius: The Life and Science of Richard Feynman* (1992) | — |
| 27 | Britannica: Richard Feynman | `https://www.britannica.com/biography/Richard-Feynman` |
| 28 | Sotheby's 2022 拍品说明（Feynman 绘 Dirac 像，含书目与 Wigner 评价） | `https://www.lotsearch.de/lot/feynman-richard-p-p-aul-a-drien-m-aurice-dirac-br-pen-ink-on-58743118` |
| 29 | Freeman Dyson, "Wise Man," *NYRB* (2005-10-20) | `http://www.nybooks.com/articles/18350` |
| 30 | HuffPost / dltn.io 对《Surely You're Joking》"A Different Box of Tools" 的段落转录 | `https://www.huffpost.com/entry/mental-models-how-intelligent-people-solve-unsolvable-problems_n_9263496` |
| 31 | Templacity 对 "Feynman Technique" 起源的溯源（含 Scott Young 2011 / Farnam Street 2012 定位） | `https://templacity.com/remarkable/feynman-technique/` |
| 32 | Gribbin & Gribbin《Richard Feynman: A Life in Science》转述的父亲教育细节 | `http://thinkingallowed1.blogspot.com/2008/05/melville-feynmans-influence.html`（博客转录，低可信，仅作线索） |
| 33 | CERN Courier 对《Feynman's Tips on Physics》的书评 | `https://cerncourier.com/a/feynmans-tips-on-physics-problem-solving-supplement-to-the-feynman-lectures-on-physics` |
| 34 | NanoWerk 对 1959 演讲与两笔奖金的报道 | `https://www.nanowerk.com/nanotechnology-news/newsid=45143.php` |

### 统计
- **一手来源：18 条**（含 8 件 Caltech/Nobel/NASA 机构存档或官方转录）
- **二手来源：16 条**（其中权威期刊/出版社 8 条，引语索引与媒体转录 8 条）
- **一手 : 二手 ≈ 1.1 : 1**（核心论点 A–I 全部有一手支撑）
- **采信的引语总数：约 60 条**，其中 45 条可定位到书名+章节+页码或演讲名+日期。
- **存疑/已排除：11 条**（见 §6）

---

## 摘要（≤800字）

**关键发现。** 从 18 条一手来源（Caltech 档案、Nobel 演讲、APS 官方转录、Messenger/Robb 讲座录音、原书页码定位）中提取出 9 条反复 ≥3 次的核心论点：A 理解=能重建（黑板句 / *Feynman Lectures on Computation* Ch.1 / 鸟的故事 / "they learn by rote" / Goodstein 的大一新生测试，共 7 处）；B 实验为唯一裁判 + 猜→推→比对（FLP I-1-1 / *Character* ch.7 / QED / *Meaning of It All*，5 处）；C 不许骗自己 + "向后弯腰"式诚实（1964 Galileo 早于 1974 Cargo Cult 十年）/《What Do You Care》/ Rogers 报告，6 处；D 无知与怀疑是引擎（1955 → 1981，6 处）；E 反权威反名相（5 处）；F 自然的想象力大于人（4 处）；G 局部蕴含整体 + 简单性信号（4 处）；H 乐趣驱动（5 处）；I 多表征多工具（5 处，含 "six or seven different theoretical representations" 与 "The same equations have the same solutions"）。

**一手/二手比例**：18 : 16 ≈ 1.1 : 1，核心论点 100% 有一手支撑。

**矛盾（已记录，未调和）**：① FLP 序言的"失败"自评 vs Sands 说那是 65 分均分打击下对着录音机即兴口授、Goodstein/Neugebauer 的"学生流失"说又被 Sands 反驳；② Nobel 演讲"不必看他们做了什么" vs *Lectures on Computation*"读别人的做法也有价值"；③ 实验唯一裁判 vs "靠美与简洁认出真理"；④ "长线织锦"的本体论乐观 vs QED p.149"物理学家想象力贫乏"的认识论自嘲；⑤ 同章既说自然是数学语言又说物理最终可能不需要数学；⑥ "不在乎荣誉" vs Gell-Mann 说他精心经营人设。

**存疑不采纳 11 条**：Shut up and calculate（Mermin 自创）、Physics is like sex、ornithology is to birds、If you can't explain it simply、Religion is a culture of faith、There are no miracle people、Mrs. Chown 便条（原句不同）、**"费曼学习法"四步（Scott Young 2011 发明，非他本人）**、Scientists are explorers、truth 句的 "always" 增字、遗言两版本冲突。

**候选心智模型（8 个，按可信度排序）**
1. **重建判据**：不能从零重建 = 不理解（黑板 + Ch.1 自述 + 大一新生测试）。最硬。
2. **猜—推—比对循环**：先猜、算后果、交给自然裁决；猜不丢人，不猜才丢人。
3. **后仰式诚实**：主动提供一切可能推翻自己的细节；诚信是操作而非态度。
4. **无知作为引擎**：承认无知 + 保留怀疑 = 唯一能持续进步的结构（trial and error 的制度化）。
5. **名相 ≠ 实质**：对权威无敬意，只看"他从哪开始、到哪结束、是否合理"；用幼稚但相关的问题做探测。
6. **不让自然迁就我**：自然的想象力大于人；"悖论"只是现实与你以为的现实之冲突。
7. **最小支点 + 最大展开**：长线织锦、一个句子装下整个世界、同一方程同一解、简单性作为真理信号。
8. **先拆"物理上是否被禁止"再谈工程**：1959 纳米、1982 量子计算同一模板；并把问题外包成公开招标。

**文件路径**：`C:\Users\cqs6017\.workbuddy\skills\feynman-perspective\references\research\01-writings.md`
