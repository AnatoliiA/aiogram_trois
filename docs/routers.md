<spam>$ Created by Kamarali Anatolii at 14:35 14.11.2023 file: routers </spam><br>
$ проект название aiogramproject

# Роутеры
Router can route update, and it nested update types like messages, <br>
callback query, polls and all other event types.
Event handlers can be registered in observer by two ways.<br>

1. By observer method - router.<event_type>.register(handler, <filters, ...>)

    async def customfunc(message: Message):
        await message.reply(message.text)
    
    routerstart.message.register(customfunc, F.text == 'hello')


2. By decorator - @router.<event_type>(<filters, ...>)

    @router.message()<br>
    async def message_handler(message: types.Message) -> Any: pass<br>
    
    @router.edited_message()<br>
    async def edited_message_handler(edited_message: types.Message) -> Any: pass<br>
    
    module1<br>
    router2 = Router()<br>
    
    @router2.message()<br>
        ...<br>
        
        from module_2 <br>
        import router2 <br>
        
        
        router1 = Router()<br>
        router1.include_router(router2)<br>