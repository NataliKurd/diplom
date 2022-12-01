from vkbottle import KeyboardButtonColor, Text


def keyboard_init(keyboard_bank):
    keyboard_bank['start_keyboard'].add(Text('����� �� ����������',
                                             payload={"command": 'manual'}
                                             )
                                        )
    keyboard_bank['start_keyboard'].row()
    keyboard_bank['start_keyboard'].add(Text('����� ������-�� ��� ����',
                                             payload={"command": 'smart'}
                                             ),
                                        color=KeyboardButtonColor.POSITIVE
                                        )
    keyboard_bank['start_keyboard'].row()
    

    keyboard_bank['gender_choise'].add(Text("�������",
                                            payload={"command": '2'}
                                            )
                                       )
    keyboard_bank['gender_choise'].add(Text("�������",
                                            payload={"command": '1'}
                                            )
                                       )
    keyboard_bank['status_choise-1'].add(Text("�� �������",
                                              payload={"command": "single"}
                                              )
                                         )
    keyboard_bank['status_choise-1'].add(Text("�����������",
                                              payload={"command": "meets"}))
    keyboard_bank['status_choise-1'].row()
    keyboard_bank['status_choise-1'].add(Text("����������",
                                              payload={"command": "engaged"}))
    keyboard_bank['status_choise-1'].add(Text("�������",
                                              payload={"command": "married"}))
    keyboard_bank['status_choise-1'].row()
    keyboard_bank['status_choise-1'].add(Text("�� ������",
                                              payload={"command": "complicated"}))
    keyboard_bank['status_choise-1'].add(Text("� �������� ������",
                                              payload={"command": "search"}))
    keyboard_bank['status_choise-1'].row()
    keyboard_bank['status_choise-1'].add(Text("��������",
                                              payload={"command": "in love"}))
    keyboard_bank['status_choise-1'].add(Text("� ����������� �����",
                                              payload={"command": "civil marriage"}))

    keyboard_bank['status_choise-2'].add(Text("�� �����",
                                              payload={"command": "single"}))
    keyboard_bank['status_choise-2'].add(Text("�����������",
                                              payload={"command": "meets"}))
    keyboard_bank['status_choise-2'].row()
    keyboard_bank['status_choise-2'].add(Text("���������",
                                              payload={"command": "engaged"}))
    keyboard_bank['status_choise-2'].add(Text("�����",
                                         payload={"command": "married"}))
    keyboard_bank['status_choise-2'].row()
    keyboard_bank['status_choise-2'].add(Text("�� ������",
                                         payload={"command": "complicated"}))
    keyboard_bank['status_choise-2'].add(Text("� �������� ������",
                                         payload={"command": "search"}))
    keyboard_bank['status_choise-2'].row()
    keyboard_bank['status_choise-2'].add(Text("�������",
                                         payload={"command": "in love"}))
    keyboard_bank['status_choise-2'].add(Text("� ����������� �����",
                                         payload={"command": "civil marriage"})
                                         )

    keyboard_bank['end_keyboard'].add(Text('����� ������',
                                           payload={"command": 'again'}),
                                      color=KeyboardButtonColor.POSITIVE
                                      )
    keyboard_bank['end_keyboard'].row()
    keyboard_bank['end_keyboard'].add(Text('� ���� ��� �����',
                                           payload={"command": 'end'}
                                           )
                                      )