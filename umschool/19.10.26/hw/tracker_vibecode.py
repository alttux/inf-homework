from claude_code import agent

super_mega_zummer_coder = agent.super_mega_zummer_coder().setup()

super_mega_zummer_coder.systemprompt('Как надо делай как не надо не делай')
super_mega_zummer_coder.systemprompt.start_work(
    message='напиши трекер привычек, в нем должно быть все что надо, что не надо значит не надо',
    price='10$ & 100$ & 200$'
)

while super_mega_zummer_coder.work.is_working():
    programmer.drink_coffee()

super_mega_zummer_coder.systemprompt().git_hub.
