using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.AllowDrop = true;
            pictureBox2.AllowDrop = true;
        }
        private void picturebox1_DragDrop(object sender, DragEventArgs e)
        {
            var data = e.Data.GetData(DataFormats.FileDrop);
            if (data != null) { 
                var filenames = data as string[];
                if(filenames.Length > 0)
                    pictureBox1.Image = Image.FromFile(filenames[0]);
            }
        }

        private void Picturebox1_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Copy;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
                pictureBox1.DoDragDrop(pictureBox1.Image, DragDropEffects.Copy);
        }
        private void pictureBox2_DragDrop(object sender, DragEventArgs e)
        {
            pictureBox2.Image = (Bitmap)e.Data.GetData(DataFormats.Bitmap, true);
        }

        private void picturebox2_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.Bitmap) && (e.AllowedEffect & DragDropEffects.Copy) != 0)
                e.Effect = DragDropEffects.Copy;
            else
                e.Effect = DragDropEffects.None;

            {

            }
        }

        
    }
}
