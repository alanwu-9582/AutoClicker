# PyQt5 Cheat Sheet

## QLabel
- **setText(text: str):** 設置標籤文字
- **text(): str:** 獲取標籤文字

## QPushButton
- **setText(text: str):** 設置按鈕文字
- **text(): str:** 獲取按鈕文字
- **clicked.connect(callback):** 連接按鈕點擊事件到自定義方法

## QLineEdit
- **setText(text: str):** 設置文本框文字
- **text(): str:** 獲取文本框文字
- **returnPressed.connect(callback):** 連接回車鍵按下事件到自定義方法

## QTextEdit
- **setPlainText(text: str):** 設置多行文本框純文本
- **toPlainText(): str:** 獲取多行文本框純文本

## QCheckBox
- **setText(text: str):** 設置勾選框文字
- **text(): str:** 獲取勾選框文字
- **isChecked(): bool:** 檢查是否被選中
- **stateChanged.connect(callback):** 連接狀態變化事件到自定義方法

## QRadioButton
- **setText(text: str):** 設置單選按鈕文字
- **text(): str:** 獲取單選按鈕文字
- **isChecked(): bool:** 檢查是否被選中
- **toggled.connect(callback):** 連接切換事件到自定義方法

## QComboBox
- **addItem(text: str):** 添加項目
- **currentText(): str:** 獲取當前選中的文本
- **currentIndex(): int:** 獲取當前選中的索引
- **currentIndexChanged.connect(callback):** 連接選擇變化的事件到自定義方法

## QListWidget
- **addItem(item: QListWidgetItem):** 添加列表項目
- **currentItem(): QListWidgetItem:** 獲取當前選中的項目
- **currentRow(): int:** 獲取當前選中的行數
- **itemClicked.connect(callback):** 連接點擊項目的事件到自定義方法

## QSlider
- **setValue(value: int):** 設置滑塊的值
- **value(): int:** 獲取滑塊的值
- **valueChanged.connect(callback):** 連接值變化的事件到自定義方法

## QProgressBar
- **setValue(value: int):** 設置進度條的值
- **value(): int:** 獲取進度條的值

## QFileDialog
- **getOpenFileName(parent, caption, directory, filter):** 打開文件對話框，獲取選中文件的路徑
- **getSaveFileName(parent, caption, directory, filter):** 打開保存文件對話框，獲取選中文件的路徑
- **folder_dialog.getExistingDirectory(self, "Select Folder")** 取得資料夾路徑

## QMainWindow
- **statusBar(): QStatusBar:** 獲取主窗口的狀態欄
- **setCentralWidget(widget):** 設置主窗口的中央部件

## QStatusBar
- **showMessage(msg, duration)** 顯示狀態訊息

## QWidget
- **setFixedSize(width, height):** 設置窗口的固定大小

## Signals and Slots
- **connect(callback):** 連接信號和槽，當信號發射時調用回調函數
- **disconnect(callback):** 斷開信號和槽的連接

## Event Handling
- **eventFilter(obj, event):** 自定義事件過濾器方法，用於特定事件的處理
- **installEventFilter(obj):** 安裝事件過濾器到指定對象
- **removeEventFilter(obj):** 移除事件過濾器

## QMessageBox
- **information(parent, title, text):** 顯示信息對話框
- **question(parent, title, text, buttons):** 顯示詢問對話框
- **warning(parent, title, text):** 顯示警告對話框
- **critical(parent, title, text):** 顯示致命錯誤對話框

## QInputDialog
- **getText(parent, title, label):** 獲取文字輸入對話框中的用戶輸入
- **getInt(parent, title, label, value, min, max, step):** 獲取整數輸入對話框中的用戶輸入

## QTabWidget
- **currentIndex()** 獲取當前選中標籤頁的索引
