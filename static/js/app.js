var toolbarOptions = [

    ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
      
    [{ 'header': 1 }, { 'header': 2 }],               // custom button values
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
    [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
    [{ 'direction': 'rtl' }],                         // text direction
  
    [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
    [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
  
    // dropdown with defaults from theme
    [{ 'color': [] }, { 'background': [] }],
    [{ 'font': [] }],
    [{ 'align': [] }],
  
    ['clean'] 
                                            // remove formatting button
  ];

var quill = new Quill('#text-editor', {
    modules: {
      syntax: true,
      toolbar: toolbarOptions
    },
    placeholder: 'داستان جدید؟ یا چپتر جدید؟',
    theme: 'snow'
  });


  // برای راست چین کردن
  var content = quill.getContents();
  quill.setSelection(0 , quill.getLength())
  document.querySelector(".ql-direction").click();
  quill.setSelection(0 , 0);