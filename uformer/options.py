import os
import paddle


class Options:
    """docstring for Options"""
    def __init__(self):
        pass

    def init(self, parser):
        parser.add_argument('--batch_size', type=int, default=32, help=\
            'batch size')
        parser.add_argument('--nepoch', type=int, default=60, help=\
            'training epochs')
        parser.add_argument('--train_workers', type=int, default=8, help=\
            'train_dataloader workers')
        parser.add_argument('--eval_workers', type=int, default=8, help=\
            'eval_dataloader workers')
        parser.add_argument('--dataset', type=str, default='SIDD')
        parser.add_argument('--pretrain_weights', type=str, default=\
            '/home/aistudio/uformer/log/Uformer_/models_ssim_l1/model_best1.pdparams', help=\
            'path of pretrained_weights')
        parser.add_argument('--optimizer', type=str, default='adamw', help=\
            'optimizer for training')
        parser.add_argument('--lr_initial',
                            type=float,
                            default=0.0002,
                            help='initial learning rate')
        parser.add_argument('--weight_decay',
                            type=float,
                            default=0.02,
                            help='weight decay')
        parser.add_argument('--gpu', type=str, default='0,1', help='GPUs')
        parser.add_argument('--arch', type=str, default='Uformer', help=\
            'archtechture')
        parser.add_argument('--mode', type=str, default='denoising', help=\
            'image restoration mode')
        parser.add_argument('--save_dir', type=str, default=\
            '/home/ma-user/work/deNoTr/log', help='save dir')
        parser.add_argument('--save_images',
                            action='store_true',
                            default=False)
        parser.add_argument('--env', type=str, default='_', help='env')
        parser.add_argument('--checkpoint', type=int, default=5, help=\
            'checkpoint')
        parser.add_argument('--norm_layer', type=str, default=\
            'nn.LayerNorm', help='normalize layer in transformer')
        parser.add_argument('--embed_dim', type=int, default=32, help=\
            'dim of emdeding features')
        parser.add_argument('--win_size', type=int, default=8, help=\
            'window size of self-attention')
        parser.add_argument('--token_projection', type=str, default=\
            'linear', help='linear/conv token projection')
        parser.add_argument('--token_mlp', type=str, default='leff', help=\
            'ffn/leff token mlp')
        parser.add_argument('--att_se',
                            action='store_true',
                            default=False,
                            help='se after sa')
        parser.add_argument('--vit_dim', type=int, default=256, help=\
            'vit hidden_dim')
        parser.add_argument('--vit_depth', type=int, default=12, help=\
            'vit depth')
        parser.add_argument('--vit_nheads', type=int, default=8, help=\
            'vit hidden_dim')
        parser.add_argument('--vit_mlp_dim', type=int, default=512, help=\
            'vit mlp_dim')
        parser.add_argument('--vit_patch_size', type=int, default=16, help=\
            'vit patch_size')
        parser.add_argument('--global_skip', action='store_true', default=False, help='global skip connection')
        parser.add_argument('--local_skip', action='store_true', default=False, help='local skip connection')
        parser.add_argument('--vit_share',
                            action='store_true',
                            default=False,
                            help='share vit module')
        parser.add_argument('--train_ps',
                            type=int,
                            default=128,
                            help='patch size of training sample')
        parser.add_argument('--resume', action='store_true', default=True)
        parser.add_argument('--train_dir',
                            type=str,
                            default='/home/aistudio/demoire/train',
                            help='dir of train data')
        parser.add_argument('--val_dir',
                            type=str,
                            default='/home/aistudio/demoire/val',
                            help='dir of train data')
        parser.add_argument('--warmup',
                            action='store_true',
                            default=False,
                            help='warmup')
        parser.add_argument('--warmup_epochs',
                            type=int,
                            default=3,
                            help='epochs for warmup')
        return parser
